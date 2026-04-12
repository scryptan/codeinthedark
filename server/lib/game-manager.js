export class GameManager {
  constructor() {
    this.reset();
  }

  countPassedElements = (data) => ({
    total: data.length,
    passed: data.filter(item => item.isPassed).length
  });

  reset() {
    this.current = null;
    this.codes = { 1: "", 2: "" };
    this.codeCheckerResults = { 1: "", 2: "" };
  }

  start(taskId, duration, defaultCodeTemplate) {
    this.current = { taskId, duration, startAt: Date.now() };
    this.codes = { 1: defaultCodeTemplate, 2: defaultCodeTemplate };
    this.codeCheckerResults = { 1: "", 2: "" };
  }

  stop() {
    this.reset();
  }

  submitCode(player, code) {
    this.codes[player] = code;
  }

  setCodeCheckerResult(player, result) {
    const playerId = Number(player);
    if (playerId !== 1 && playerId !== 2) {
      return;
    }

    if (!result || !result.status || result.status === 'processing') {
      this.codeCheckerResults[playerId] = "";
      return;
    }

    const hasErrorLogs = result.status !== "testsPassed" && Array.isArray(result.logs) && result.logs.length > 0;

    this.codeCheckerResults[playerId] = {
      status: result.status,
      isSussesful: result.status === "testsPassed",
      error: hasErrorLogs ? result.logs.map(str => str.replace(/\n/g, ' ')).join('\n') : null,
      testsResult: result.tests === null ? null : this.countPassedElements(result.tests),
    };
  }

  getState() {
    if (!this.current) {
      return { taskId: null, duration: 0, timeLeft: 0, codes: this.codes, codeCheckerResults: this.codeCheckerResults };
    }
    const now = Date.now();
    const end = this.current.startAt + this.current.duration * 1000;
    return {
      taskId: this.current.taskId,
      duration: this.current.duration,
      timeLeft: Math.max(0, Math.ceil((end - now) / 1000)),
      codes: this.codes,
      codeCheckerResults: this.codeCheckerResults,
    };
  }
}
