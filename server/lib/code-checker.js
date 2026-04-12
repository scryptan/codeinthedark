import crypto from "crypto";
import { copyFile, mkdtemp, rm, writeFile } from "fs/promises";
import { tmpdir } from "os";
import { dirname, join, resolve } from "path";
import { fileURLToPath } from "url";
import { GenericContainer } from "testcontainers";
import { getFileContents } from "./tasks.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const RUNNER_SOURCE = resolve(__dirname, "python-runner.py");

const PROCESSING_RESULT = {
  status: "processing",
  tests: null,
  logs: null,
};

export class CodeChecker {
  constructor() {
    this.results = new Map();
    this.dockerImage = process.env.PYTHON_DOCKER_IMAGE || "python:3.12-alpine";
    this.timeoutMs = Number(process.env.CODE_CHECK_TIMEOUT_MS || 10000);
    this.maxLogLength = Number(process.env.CODE_CHECK_MAX_LOG_LENGTH || 10000);
  }

  run(code, taskId) {
    const requestId = crypto.randomUUID();
    this.results.set(requestId, PROCESSING_RESULT);
    this.execute(requestId, code, taskId);
    return requestId;
  }

  async getResult(requestId) {
    return this.results.get(requestId) || {
      status: "runtimeError",
      tests: null,
      logs: ["Unknown request id"],
    };
  }

  async execute(requestId, code, taskId) {
    let workspacePath;

    try {
      workspacePath = await mkdtemp(join(tmpdir(), "codeinthedark-"));

      const testsPy = await getFileContents(taskId, "tests.py", "utf-8");
      await writeFile(join(workspacePath, "solution.py"), code, "utf-8");
      await writeFile(join(workspacePath, "tests.py"), testsPy, "utf-8");
      await copyFile(RUNNER_SOURCE, join(workspacePath, "runner.py"));

      const runResult = await this.runContainer(workspacePath);

      if (runResult.timedOut) {
        this.results.set(requestId, {
          status: "timeLimit",
          tests: null,
          logs: ["Execution timed out"],
        });
        return;
      }

      const result = this.parseRunnerResult(runResult.stdout, runResult.stderr);
      this.results.set(requestId, result);
    } catch (error) {
      this.results.set(requestId, {
        status: "runtimeError",
        tests: null,
        logs: this.limitLogs([error?.message || String(error)]),
      });
    } finally {
      if (workspacePath) {
        await rm(workspacePath, { recursive: true, force: true });
      }
    }
  }

  runContainer(workspacePath) {
    return this.runInTestcontainer(workspacePath);
  }

  async runInTestcontainer(workspacePath) {
    let container;

    try {
      container = await new GenericContainer(this.dockerImage)
        .withEnvironment({ PYTHONDONTWRITEBYTECODE: "1" })
        .withWorkingDir("/workspace")
        .withBindMounts([{ source: workspacePath, target: "/workspace", mode: "rw" }])
        .withNetworkMode("none")
        .withCommand(["sh", "-c", "sleep 300"])
        .start();

      const execution = container.exec(["python", "runner.py"]);
      const timedExecution = await this.withTimeout(execution, this.timeoutMs);
      if (timedExecution.timedOut) {
        return { timedOut: true, stdout: "", stderr: "Execution timed out" };
      }

      const execResult = timedExecution.result || {};
      const stdout = execResult.output || execResult.stdout || "";
      const stderrOutput = execResult.stderr || "";
      const exitCode = execResult.exitCode;

      if (exitCode === 0) {
        return { timedOut: false, stdout, stderr: stderrOutput };
      }

      return {
        timedOut: false,
        stdout,
        stderr: stderrOutput || `Runner exited with code ${exitCode}`,
      };
    } finally {
      if (container) {
        await container.stop();
      }
    }
  }

  async withTimeout(promise, timeoutMs) {
    const timeoutPromise = new Promise((resolve) => {
      setTimeout(() => resolve({ timedOut: true }), timeoutMs);
    });

    const result = await Promise.race([
      promise.then((value) => ({ timedOut: false, result: value })),
      timeoutPromise,
    ]);

    return result;
  }

  parseRunnerResult(stdout, stderr) {
    const output = stdout.trim();
    if (!output) {
      return {
        status: "runtimeError",
        tests: null,
        logs: this.limitLogs([stderr || "No output from checker"]),
      };
    }

    try {
      const jsonLine = output.split(/\r?\n/).filter(Boolean).at(-1);
      const parsed = JSON.parse(jsonLine);
      const tests = Array.isArray(parsed.tests)
        ? parsed.tests.map((test) => ({ isPassed: Boolean(test?.isPassed) }))
        : null;

      const logs = Array.isArray(parsed.logs)
        ? parsed.logs.map((x) => String(x))
        : [];

      if (stderr) {
        logs.push(stderr);
      }

      return {
        status: typeof parsed.status === "string" ? parsed.status : "runtimeError",
        tests,
        logs: this.limitLogs(logs),
      };
    } catch {
      return {
        status: "runtimeError",
        tests: null,
        logs: this.limitLogs(["Failed to parse checker output", output, stderr]),
      };
    }
  }

  limitLogs(logs) {
    const joined = (logs || []).filter(Boolean).join("\n");
    if (!joined) {
      return null;
    }

    if (joined.length <= this.maxLogLength) {
      return [joined];
    }

    return [`${joined.slice(0, this.maxLogLength)}\n... [logs truncated]`];
  }
}
