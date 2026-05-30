function getAlertBody(result) {
  return sanitizeUnittestTrace(result?.error || JSON.stringify(result, null, 2));
}

function sanitizeUnittestTrace(body) {
  return body
    .replace(/^(ERROR|FAIL): test_[\w]+ \([^)]+\)$/gm, "$1: <hidden test>")
    .replace(/\btests\.[A-Za-z_][\w]*\.test_[\w]+\b/g, "<hidden test>")
    .replace(/(File "\/workspace\/tests\.py", line \d+, in )test_[\w]+/g, "$1<hidden test>");
}

function getPassedCount(testsResult) {
  if (!testsResult) {
    return "";
  }

  return ` Passed ${testsResult.passed} from ${testsResult.total}`;
}

export function formatRunResult(result) {
  if (result?.isSussesful) {
    return {
      title: `✔ All tests passed!${getPassedCount(result.testsResult)}`,
      body: "",
      variant: "success",
    };
  }

  if (result?.status === "wrongAnswer") {
    return {
      title: `✘ Tests failed!${getPassedCount(result.testsResult)}`,
      body: getAlertBody(result),
      variant: "test-failed",
    };
  }

  if (result?.status === "runtimeError" || result?.status === "timeLimit") {
    return {
      title: "⚠ Runtime error",
      body: getAlertBody(result),
      variant: "error",
    };
  }

  return {
    title: "⚠ Test result",
    body: getAlertBody(result),
    variant: "error",
  };
}
