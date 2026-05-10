import io
import json
import traceback
import unittest
from contextlib import redirect_stderr, redirect_stdout


def extract_assertion_messages(formatted_err: str):
    """Extract human-facing AssertionError messages from unittest formatted traceback."""
    if not formatted_err:
        return []

    msgs = []
    for line in formatted_err.splitlines():
        # unittest formats failures as "AssertionError: <message>" on one line.
        if line.startswith("AssertionError:"):
            msg = line.split("AssertionError:", 1)[1].strip()
            if not msg:
                continue

            # Prefer custom assertion message if present.
            # Example: "False is not true : <custom>" or "False != True : <custom>"
            if " : " in msg:
                msg = msg.split(" : ", 1)[1].strip()

            msgs.append(msg)
    return msgs


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
                # Keep output minimal; we send structured info via JSON payload.
                runner = unittest.TextTestRunner(stream=captured_output, verbosity=1)
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
                    # For runtime errors return full traceback output.
                    logs = captured_output.getvalue().strip()
                    logs_payload = [logs] if logs else []
                else:
                    status = "wrongAnswer"
                    # For wrong answers, return only explicit AssertionError messages.
                    # Task tests should provide a helpful message, e.g.
                    # "1 2 3 -> expected 8, actual 1" to avoid leaking test names.
                    messages = []
                    for _, formatted_err in (result.failures or []):
                        messages.extend(extract_assertion_messages(formatted_err))
                    for _, formatted_err in (result.errors or []):
                        messages.extend(extract_assertion_messages(formatted_err))

                    # Fallback: if no explicit messages were provided, return a generic line.
                    logs_payload = messages if messages else ["Wrong answer"]

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
