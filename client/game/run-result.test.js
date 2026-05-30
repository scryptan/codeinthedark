import { describe, expect, it } from "vitest";

import { formatRunResult } from "./run-result";

describe("formatRunResult", () => {
  it("formats successful results with the passed tests count", () => {
    expect(
      formatRunResult({
        isSussesful: true,
        testsResult: { passed: 7, total: 7 },
      }),
    ).toEqual({
      title: "✔ All tests passed! Passed 7 from 7",
      body: "",
      variant: "success",
    });
  });

  it("formats failed tests with the full alert body", () => {
    const result = {
      status: "wrongAnswer",
      error: "AssertionError: expected 4\nactual 5",
      testsResult: { passed: 2, total: 5 },
    };

    expect(formatRunResult(result)).toEqual({
      title: "✘ Tests failed! Passed 2 from 5",
      body: result.error,
      variant: "test-failed",
    });
  });

  it("formats runtime errors with the full alert body", () => {
    const result = {
      status: "runtimeError",
      error: "Traceback (most recent call last):\nNameError: name 'x' is not defined",
      testsResult: null,
    };

    expect(formatRunResult(result)).toEqual({
      title: "⚠ Runtime error",
      body: result.error,
      variant: "error",
    });
  });

  it("hides unittest test names from tracebacks", () => {
    const result = {
      status: "runtimeError",
      error: `======================================================================
ERROR: test_another_simple_palindrome (tests.PalindromeTests.test_another_simple_palindrome)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/tests.py", line 40, in test_another_simple_palindrome
    self.assert_case("madam", True)
  File "/workspace/tests.py", line 8, in assert_case
    actual = solve(input_string)
             ^^^^^^^^^^^^^^^^^^^
  File "/workspace/solution.py", line 2, in solve
    return Tru
           ^^^
NameError: name 'Tru' is not defined. Did you mean: 'True'?`,
      testsResult: null,
    };

    const formatted = formatRunResult(result);

    expect(formatted.body).not.toContain("test_another_simple_palindrome");
    expect(formatted.body).not.toContain("tests.PalindromeTests");
    expect(formatted.body).toContain("ERROR: <hidden test>");
    expect(formatted.body).toContain('File "/workspace/tests.py", line 40, in <hidden test>');
    expect(formatted.body).toContain("NameError: name 'Tru' is not defined");
  });

  it("falls back to the same JSON text the alert used", () => {
    const result = {
      status: "unknown",
      error: "",
      testsResult: null,
      logs: ["Something odd happened"],
    };

    expect(formatRunResult(result)).toEqual({
      title: "⚠ Test result",
      body: JSON.stringify(result, null, 2),
      variant: "error",
    });
  });
});
