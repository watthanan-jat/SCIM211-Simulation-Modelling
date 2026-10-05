const editor = document.querySelector("#code-editor");
const fileInput = document.querySelector("#code-file");
const fileName = document.querySelector("#file-name");
const loadTemplateButton = document.querySelector("#load-template");
const downloadButton = document.querySelector("#download-code");
const runButton = document.querySelector("#run-check");
const stopButton = document.querySelector("#stop-check");
const status = document.querySelector("#runtime-status");
const output = document.querySelector("#checker-output");
const badge = document.querySelector("#result-badge");

const storageKey = "scim211-cafe-model-draft-v1";
let worker = null;
let pendingSource = null;
let workerReady = false;
let compatibilityPyodidePromise = null;
let compatibilityRunning = false;

function setStatus(message, busy = false) {
  status.textContent = message;
  status.classList.toggle("busy", busy);
}

function setBadge(kind, label) {
  badge.className = `result-badge ${kind}`;
  badge.textContent = label;
}

function setRunning(running) {
  runButton.disabled = running;
  stopButton.disabled = !running;
  fileInput.disabled = running;
  loadTemplateButton.disabled = running;
}

function saveDraft() {
  try {
    localStorage.setItem(storageKey, editor.value);
  } catch (_error) {
    // The editor remains usable when browser storage is unavailable.
  }
}

function loadDraft() {
  try {
    const draft = localStorage.getItem(storageKey);
    if (draft) {
      editor.value = draft;
      fileName.textContent = "Restored local draft";
    }
  } catch (_error) {
    // Ignore unavailable browser storage.
  }
}

function stopWorker(message = "Checker stopped. Run again to restart it.") {
  if (worker) {
    worker.terminate();
    worker = null;
  }
  pendingSource = null;
  workerReady = false;
  setRunning(false);
  setStatus(message, false);
}

function showReport(report) {
  output.textContent = report.lines.join("\n");
  setBadge(report.passed ? "pass" : "fail", report.passed ? "Pass" : "Fail");
  setStatus(report.passed ? "All readiness checks passed" : "Readiness check failed", false);
  setRunning(false);
  pendingSource = null;
}

async function initialiseCompatibilityRuntime() {
  const { loadPyodide } = await import("https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide.mjs");
  const runtime = await loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/"
  });
  await runtime.loadPackage("pandas");
  const checkerResponse = await fetch("mini-project-browser-checker.py", { cache: "no-store" });
  if (!checkerResponse.ok) throw new Error(`Could not load checker core: HTTP ${checkerResponse.status}`);
  await runtime.runPythonAsync(await checkerResponse.text());
  return runtime;
}

async function runCompatibilityCheck(source) {
  if (compatibilityRunning || !source) return;
  compatibilityRunning = true;

  if (worker) {
    worker.terminate();
    worker = null;
  }

  setStatus("Using browser compatibility mode", true);
  output.textContent = "The isolated worker is unavailable in this browser. Loading the compatibility checker…";

  try {
    if (!compatibilityPyodidePromise) compatibilityPyodidePromise = initialiseCompatibilityRuntime();
    const runtime = await compatibilityPyodidePromise;
    setStatus("Loading packages used by your file", true);
    await runtime.loadPackagesFromImports(source);
    runtime.globals.set("student_source", source);
    setStatus("Running checks in compatibility mode", true);
    const reportJson = await runtime.runPythonAsync("check_source_json(student_source)");
    showReport(JSON.parse(reportJson));
  } catch (error) {
    compatibilityPyodidePromise = null;
    output.textContent = `FAIL\nThe browser checker could not start.\n${error.message || String(error)}`;
    setBadge("fail", "Fail");
    setStatus("Checker could not start", false);
    setRunning(false);
    pendingSource = null;
  } finally {
    compatibilityRunning = false;
  }
}

function startWorker(source) {
  pendingSource = source;
  workerReady = false;
  setRunning(true);
  setBadge("running", "Running");
  output.textContent = "Starting the browser Python runtime…";
  setStatus("Loading Python runtime", true);

  worker = new Worker("mini-project-worker.js?v=20260919b", { type: "module" });

  worker.addEventListener("message", (event) => {
    const message = event.data;

    if (message.type === "status") {
      setStatus(message.message, true);
      output.textContent = message.message;
      return;
    }

    if (message.type === "ready") {
      workerReady = true;
      setStatus("Running checks", true);
      output.textContent = "Python is ready. Running the readiness checks…";
      worker.postMessage({ type: "check", source: pendingSource });
      return;
    }

    if (message.type === "result") {
      showReport(message.report);
      return;
    }

    if (message.type === "error") {
      if (!workerReady) {
        runCompatibilityCheck(pendingSource);
        return;
      }
      output.textContent = `FAIL\n${message.message}`;
      setBadge("fail", "Fail");
      setStatus("Checker error", false);
      setRunning(false);
      pendingSource = null;
    }
  });

  worker.addEventListener("error", (event) => {
    event.preventDefault();
    runCompatibilityCheck(pendingSource);
  });
}

fileInput.addEventListener("change", async () => {
  const [file] = fileInput.files;
  if (!file) return;

  if (!file.name.endsWith(".py")) {
    output.textContent = "FAIL\nChoose a Python file ending in .py.";
    setBadge("fail", "Fail");
    return;
  }

  editor.value = await file.text();
  fileName.textContent = file.name;
  saveDraft();
  setBadge("neutral", "Not run");
  output.textContent = "File loaded. Select “Run readiness check”.";
});

loadTemplateButton.addEventListener("click", async () => {
  if (editor.value.trim() && !window.confirm("Replace the editor contents with the starter template?")) return;

  try {
    const response = await fetch("mini-project-template.py", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    editor.value = await response.text();
    fileName.textContent = "Starter template";
    saveDraft();
    setBadge("neutral", "Not run");
    output.textContent = "Template loaded. Complete the TODO sections before testing.";
  } catch (error) {
    output.textContent = `Could not load the template: ${error.message}`;
    setBadge("fail", "Error");
  }
});

downloadButton.addEventListener("click", () => {
  if (!editor.value.trim()) {
    output.textContent = "There is no code in the editor to download.";
    return;
  }

  const blob = new Blob([editor.value], { type: "text/x-python;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "cafe_model.py";
  link.click();
  URL.revokeObjectURL(url);
});

editor.addEventListener("input", () => {
  saveDraft();
  setBadge("neutral", "Not run");
});

editor.addEventListener("keydown", (event) => {
  if (event.key !== "Tab") return;
  event.preventDefault();
  const start = editor.selectionStart;
  const end = editor.selectionEnd;
  editor.setRangeText("    ", start, end, "end");
  saveDraft();
});

runButton.addEventListener("click", () => {
  const source = editor.value.trim();
  if (!source) {
    output.textContent = "FAIL\nPaste or upload cafe_model.py before running the checker.";
    setBadge("fail", "Fail");
    return;
  }

  if (worker) worker.terminate();
  worker = null;
  startWorker(source);
});

stopButton.addEventListener("click", () => {
  output.textContent = "The running test was stopped. Your code remains in the editor.";
  setBadge("neutral", "Stopped");
  stopWorker();
});

loadDraft();
