import { loadPyodide } from "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide.mjs";

let pyodide = null;

async function initialise() {
  self.postMessage({ type: "status", message: "Downloading the browser Python runtime…" });
  pyodide = await loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/"
  });

  self.postMessage({ type: "status", message: "Loading pandas and the readiness checker…" });
  await pyodide.loadPackage("pandas");
  const checkerResponse = await fetch("mini-project-browser-checker.py", { cache: "no-store" });
  if (!checkerResponse.ok) throw new Error(`Could not load checker core: HTTP ${checkerResponse.status}`);
  const checkerSource = await checkerResponse.text();
  await pyodide.runPythonAsync(checkerSource);
  self.postMessage({ type: "ready" });
}

const readyPromise = initialise().catch((error) => {
  self.postMessage({ type: "error", message: `${error.name}: ${error.message}` });
  throw error;
});

self.addEventListener("message", async (event) => {
  if (event.data.type !== "check") return;

  try {
    await readyPromise;
    self.postMessage({ type: "status", message: "Loading packages used by your file…" });
    await pyodide.loadPackagesFromImports(event.data.source);
    pyodide.globals.set("student_source", event.data.source);
    const reportJson = await pyodide.runPythonAsync("check_source_json(student_source)");
    self.postMessage({ type: "result", report: JSON.parse(reportJson) });
  } catch (error) {
    self.postMessage({
      type: "error",
      message: error.message || String(error)
    });
  }
});
