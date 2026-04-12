import io
import json
import traceback
import unittest
from contextlib import redirect_stderr, redirect_stdout


def flatten_tests(test_suite):
    for item in test_suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten_tests(item)
        else:
            yield item


def main():
    try:
        captured_output = io.StringIO()
        payload = None

        with redirect_stdout(captured_output), redirect_stderr(captured_output):
            suite = unittest.defaultTestLoader.discover(".", pattern="tests.py")
            tests = list(flatten_tests(suite))

            if not tests:
                payload = {
                    "status": "runtimeError",
                    "tests": None,
                    "logs": ["No tests found in tests.py"],
                }
            else:
                runner = unittest.TextTestRunner(stream=captured_output, verbosity=2)
                result = runner.run(suite)

                failed = {test.id() for test, _ in result.failures}
                errored = {test.id() for test, _ in result.errors}
                broken = failed | errored

                tests_payload = [{"isPassed": test.id() not in broken} for test in tests]

                if result.wasSuccessful():
                    status = "testsPassed"
                    logs_payload = []
                elif result.errors and not result.failures:
                    status = "runtimeError"
                    logs = captured_output.getvalue().strip()
                    logs_payload = [logs] if logs else []
                else:
                    status = "wrongAnswer"
                    logs = captured_output.getvalue().strip()
                    logs_payload = [logs] if logs else []

                payload = {
                    "status": status,
                    "tests": tests_payload,
                    "logs": logs_payload,
                }

        print(json.dumps(payload))
    except Exception:
        payload = {
            "status": "runtimeError",
            "tests": None,
            "logs": [traceback.format_exc()],
        }
        print(json.dumps(payload))


if __name__ == "__main__":
    main()
