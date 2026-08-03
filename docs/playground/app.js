"use strict";

(() => {
  const $ = (id) => document.getElementById(id);
  const integerFormatter = new Intl.NumberFormat("en-GB");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function clamp(value, minimum, maximum) {
    return Math.min(maximum, Math.max(minimum, value));
  }

  function seedToUint32(value) {
    const text = String(value).trim() || "0";
    let hash = 2166136261;
    for (let index = 0; index < text.length; index += 1) {
      hash ^= text.charCodeAt(index);
      hash = Math.imul(hash, 16777619);
    }
    return hash >>> 0;
  }

  function seededRandom(seed) {
    let state = seedToUint32(seed);
    return function random() {
      state += 0x6d2b79f5;
      let value = state;
      value = Math.imul(value ^ (value >>> 15), value | 1);
      value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
      return ((value ^ (value >>> 14)) >>> 0) / 4294967296;
    };
  }

  function createSeed() {
    if (window.crypto && window.crypto.getRandomValues) {
      const values = new Uint32Array(1);
      window.crypto.getRandomValues(values);
      return String(values[0]);
    }
    return String(Math.floor(Date.now() % 4294967295));
  }

  function cleanSeed(input) {
    const seed = input.value.trim() || createSeed();
    input.value = seed;
    return seed;
  }

  function escapeCsv(value) {
    const text = String(value);
    return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
  }

  function downloadCsv(filename, rows) {
    const csv = rows.map((row) => row.map(escapeCsv).join(",")).join("\n");
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      try {
        await navigator.clipboard.writeText(text);
        return;
      } catch {
        // Some browsers expose the Clipboard API but block it for local pages.
      }
    }
    const temporary = document.createElement("textarea");
    temporary.value = text;
    temporary.setAttribute("readonly", "");
    temporary.style.position = "fixed";
    temporary.style.opacity = "0";
    document.body.appendChild(temporary);
    temporary.select();
    const copied = document.execCommand("copy");
    temporary.remove();
    if (!copied) throw new Error("Copy command was unavailable.");
  }

  function announceCopy(statusElement, message) {
    statusElement.textContent = message;
    window.clearTimeout(statusElement.clearTimer);
    statusElement.clearTimer = window.setTimeout(() => {
      statusElement.textContent = "";
    }, 2600);
  }

  function clearCanvas(context, canvas) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "#ffffff";
    context.fillRect(0, 0, canvas.width, canvas.height);
  }

  function drawGraphFrame(context, canvas, margins, xLabel, yLabel) {
    const { left, top, right, bottom } = margins;
    const plotWidth = canvas.width - left - right;
    const plotHeight = canvas.height - top - bottom;

    clearCanvas(context, canvas);
    context.strokeStyle = "#d8e1ec";
    context.lineWidth = 1;
    context.strokeRect(left, top, plotWidth, plotHeight);
    context.fillStyle = "#607086";
    context.font = "600 14px system-ui";
    context.textAlign = "center";
    context.fillText(xLabel, left + plotWidth / 2, canvas.height - 10);
    context.save();
    context.translate(17, top + plotHeight / 2);
    context.rotate(-Math.PI / 2);
    context.fillText(yLabel, 0, 0);
    context.restore();
    return { left, top, plotWidth, plotHeight };
  }

  function setActiveTab(selectedButton) {
    const tabButtons = [...document.querySelectorAll('[role="tab"]')];
    tabButtons.forEach((button) => {
      const active = button === selectedButton;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-selected", String(active));
      button.tabIndex = active ? 0 : -1;
      $(button.getAttribute("aria-controls")).hidden = !active;
    });
    if (selectedButton.id === "pi-tab") {
      drawPi();
      drawPiGraph();
    } else {
      drawSir();
      drawSirGraph();
    }
  }

  const tabs = [...document.querySelectorAll('[role="tab"]')];
  tabs.forEach((button, index) => {
    button.addEventListener("click", () => setActiveTab(button));
    button.addEventListener("keydown", (event) => {
      if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      let nextIndex = index;
      if (event.key === "ArrowLeft") nextIndex = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "ArrowRight") nextIndex = (index + 1) % tabs.length;
      if (event.key === "Home") nextIndex = 0;
      if (event.key === "End") nextIndex = tabs.length - 1;
      tabs[nextIndex].focus();
      setActiveTab(tabs[nextIndex]);
    });
  });

  // Monte Carlo estimation of pi
  const piCanvas = $("pi-canvas");
  const piContext = piCanvas.getContext("2d");
  const piGraph = $("pi-graph");
  const piGraphContext = piGraph.getContext("2d");
  const piSeedInput = $("pi-seed");
  const piSpeedInput = $("pi-speed");
  const piSpeedValues = [10, 50, 250, 1000, 5000];
  const maximumVisiblePoints = 7000;

  const piState = {
    seed: "",
    random: seededRandom(0),
    total: 0,
    inside: 0,
    visiblePoints: [],
    history: [],
    timer: null
  };

  function currentPiSpeed() {
    return piSpeedValues[Number(piSpeedInput.value) - 1];
  }

  function updatePiSpeedLabel() {
    $("pi-speed-output").textContent = `${integerFormatter.format(currentPiSpeed())} points/tick`;
  }

  function addPiPoints(count) {
    const newVisiblePoints = [];
    for (let index = 0; index < count; index += 1) {
      const x = piState.random() * 2 - 1;
      const y = piState.random() * 2 - 1;
      const inside = x * x + y * y <= 1;
      piState.total += 1;
      if (inside) piState.inside += 1;
      newVisiblePoints.push({ x, y, inside });
    }

    piState.visiblePoints.push(...newVisiblePoints);
    if (piState.visiblePoints.length > maximumVisiblePoints) {
      piState.visiblePoints = piState.visiblePoints.slice(-maximumVisiblePoints);
    }

    const estimate = (4 * piState.inside) / piState.total;
    piState.history.push({
      n: piState.total,
      h: piState.inside,
      estimate,
      error: Math.abs(estimate - Math.PI)
    });
    updatePi();
  }

  function drawPi() {
    const width = piCanvas.width;
    const height = piCanvas.height;
    const padding = 24;
    const size = Math.min(width, height) - padding * 2;
    const left = (width - size) / 2;
    const top = (height - size) / 2;
    const centreX = width / 2;
    const centreY = height / 2;
    const radius = size / 2;

    clearCanvas(piContext, piCanvas);
    piContext.fillStyle = "#f7f9fc";
    piContext.fillRect(left, top, size, size);
    piContext.strokeStyle = "#17365d";
    piContext.lineWidth = 3;
    piContext.strokeRect(left, top, size, size);
    piContext.beginPath();
    piContext.arc(centreX, centreY, radius, 0, Math.PI * 2);
    piContext.fillStyle = "rgba(39, 103, 178, 0.055)";
    piContext.fill();
    piContext.strokeStyle = "#2767b2";
    piContext.lineWidth = 3;
    piContext.stroke();

    const pointRadius = piState.visiblePoints.length > 3500 ? 1.5 : 2.3;
    piState.visiblePoints.forEach((point) => {
      const pointX = left + ((point.x + 1) / 2) * size;
      const pointY = top + ((1 - point.y) / 2) * size;
      piContext.beginPath();
      piContext.arc(pointX, pointY, pointRadius, 0, Math.PI * 2);
      piContext.fillStyle = point.inside ? "rgba(33, 140, 104, 0.8)" : "rgba(223, 102, 88, 0.82)";
      piContext.fill();
    });
  }

  function drawPiGraph() {
    const frame = drawGraphFrame(
      piGraphContext,
      piGraph,
      { left: 62, top: 28, right: 24, bottom: 52 },
      "Number of points, N (log scale)",
      "pi_hat"
    );
    const minimumY = 0;
    const maximumY = 4.15;
    const maximumN = Math.max(10, piState.total);
    const maximumLogN = Math.log10(maximumN);
    const xFor = (n) => frame.left + (Math.log10(Math.max(1, n)) / maximumLogN) * frame.plotWidth;
    const yFor = (value) => frame.top + ((maximumY - value) / (maximumY - minimumY)) * frame.plotHeight;

    piGraphContext.font = "12px system-ui";
    piGraphContext.fillStyle = "#607086";
    piGraphContext.textAlign = "right";
    [0, 1, 2, 3, 4].forEach((tick) => {
      const y = yFor(tick);
      piGraphContext.fillText(String(tick), frame.left - 8, y + 4);
      piGraphContext.strokeStyle = "#edf1f6";
      piGraphContext.beginPath();
      piGraphContext.moveTo(frame.left, y);
      piGraphContext.lineTo(frame.left + frame.plotWidth, y);
      piGraphContext.stroke();
    });

    const piY = yFor(Math.PI);
    piGraphContext.save();
    piGraphContext.strokeStyle = "#df6658";
    piGraphContext.lineWidth = 2;
    piGraphContext.setLineDash([8, 7]);
    piGraphContext.beginPath();
    piGraphContext.moveTo(frame.left, piY);
    piGraphContext.lineTo(frame.left + frame.plotWidth, piY);
    piGraphContext.stroke();
    piGraphContext.restore();
    piGraphContext.fillStyle = "#a9362e";
    piGraphContext.textAlign = "left";
    piGraphContext.fillText("true pi", frame.left + 8, piY - 7);

    const powers = [];
    for (let power = 0; power <= Math.floor(maximumLogN); power += 1) powers.push(10 ** power);
    if (!powers.includes(maximumN)) powers.push(maximumN);
    piGraphContext.fillStyle = "#607086";
    piGraphContext.textAlign = "center";
    powers.forEach((tick) => {
      const x = xFor(tick);
      piGraphContext.fillText(integerFormatter.format(tick), x, frame.top + frame.plotHeight + 20);
    });

    if (piState.history.length === 0) {
      piGraphContext.fillStyle = "#607086";
      piGraphContext.font = "600 15px system-ui";
      piGraphContext.textAlign = "center";
      piGraphContext.fillText("Drop points to begin the graph", frame.left + frame.plotWidth / 2, frame.top + frame.plotHeight / 2);
      return;
    }

    piGraphContext.strokeStyle = "#2767b2";
    piGraphContext.lineWidth = 2.5;
    piGraphContext.lineJoin = "round";
    piGraphContext.beginPath();
    piState.history.forEach((entry, index) => {
      const x = xFor(entry.n);
      const y = yFor(clamp(entry.estimate, minimumY, maximumY));
      if (index === 0) piGraphContext.moveTo(x, y);
      else piGraphContext.lineTo(x, y);
    });
    piGraphContext.stroke();

    const latest = piState.history.at(-1);
    piGraphContext.beginPath();
    piGraphContext.arc(xFor(latest.n), yFor(clamp(latest.estimate, minimumY, maximumY)), 4.5, 0, Math.PI * 2);
    piGraphContext.fillStyle = "#17365d";
    piGraphContext.fill();
  }

  function updatePi() {
    drawPi();
    drawPiGraph();
    $("pi-total").textContent = integerFormatter.format(piState.total);
    $("pi-inside").textContent = integerFormatter.format(piState.inside);
    if (piState.total === 0) {
      $("pi-estimate").textContent = "Not yet available";
      $("pi-error").textContent = "Not yet available";
    } else {
      const estimate = (4 * piState.inside) / piState.total;
      $("pi-estimate").textContent = estimate.toFixed(6);
      $("pi-error").textContent = Math.abs(estimate - Math.PI).toFixed(6);
    }
  }

  function pausePi() {
    if (piState.timer !== null) {
      window.clearInterval(piState.timer);
      piState.timer = null;
    }
    $("pi-run").disabled = false;
    $("pi-pause").disabled = true;
  }

  function runPi() {
    if (piState.timer !== null) return;
    $("pi-run").disabled = true;
    $("pi-pause").disabled = false;
    piState.timer = window.setInterval(() => addPiPoints(currentPiSpeed()), 150);
  }

  function resetPi() {
    pausePi();
    piState.seed = cleanSeed(piSeedInput);
    piState.random = seededRandom(piState.seed);
    piState.total = 0;
    piState.inside = 0;
    piState.visiblePoints = [];
    piState.history = [];
    updatePi();
  }

  document.querySelectorAll(".pi-drop").forEach((button) => {
    button.addEventListener("click", () => addPiPoints(Number(button.dataset.count)));
  });
  $("pi-run").addEventListener("click", runPi);
  $("pi-pause").addEventListener("click", pausePi);
  $("pi-reset").addEventListener("click", resetPi);
  piSpeedInput.addEventListener("input", updatePiSpeedLabel);
  $("pi-new-seed").addEventListener("click", () => {
    piSeedInput.value = createSeed();
    resetPi();
  });
  $("pi-download").addEventListener("click", () => {
    const rows = [["N", "H", "pi_hat", "absolute_error", "seed"]];
    piState.history.forEach((entry) => rows.push([
      entry.n,
      entry.h,
      entry.estimate.toFixed(10),
      entry.error.toFixed(10),
      piState.seed
    ]));
    if (piState.history.length === 0) rows.push([0, 0, "", "", piState.seed]);
    downloadCsv(`scim211-pi-seed-${piState.seed}.csv`, rows);
    announceCopy($("pi-copy-status"), `CSV prepared with ${rows.length - 1} result row${rows.length === 2 ? "" : "s"}.`);
  });
  $("pi-copy").addEventListener("click", async () => {
    const estimate = piState.total ? (4 * piState.inside) / piState.total : null;
    const summary = [
      "SCIM211 Monte Carlo Pi experiment",
      `Seed: ${piState.seed}`,
      `N: ${piState.total}`,
      `H: ${piState.inside}`,
      `pi_hat: ${estimate === null ? "not available" : estimate.toFixed(10)}`,
      `Absolute error: ${estimate === null ? "not available" : Math.abs(estimate - Math.PI).toFixed(10)}`,
      "Rule: sample (x,y) uniformly from [-1,1]^2; inside when x^2 + y^2 <= 1."
    ].join("\n");
    try {
      await copyText(summary);
      announceCopy($("pi-copy-status"), "Experiment summary copied.");
    } catch {
      announceCopy($("pi-copy-status"), "Copy was unavailable in this browser.");
    }
  });

  // SIR interacting-particle epidemic
  const sirCanvas = $("sir-canvas");
  const sirContext = sirCanvas.getContext("2d");
  const sirGraph = $("sir-graph");
  const sirGraphContext = sirGraph.getContext("2d");
  const sirInputs = {
    n: $("sir-n"),
    initial: $("sir-initial"),
    p: $("sir-p"),
    q: $("sir-q"),
    speed: $("sir-speed"),
    seed: $("sir-seed")
  };

  const sirState = {
    seed: "",
    random: seededRandom(0),
    states: [],
    time: 0,
    history: [],
    peak: 0,
    peakTime: 0,
    duration: null,
    timer: null,
    animationFrame: null,
    changed: []
  };

  function sirParameters() {
    const n = Number(sirInputs.n.value);
    return {
      n,
      initial: clamp(Number(sirInputs.initial.value), 1, n),
      p: Number(sirInputs.p.value),
      q: Number(sirInputs.q.value),
      speed: Number(sirInputs.speed.value)
    };
  }

  function updateSirLabels() {
    const n = Number(sirInputs.n.value);
    sirInputs.initial.max = String(n);
    if (Number(sirInputs.initial.value) > n) sirInputs.initial.value = String(n);
    $("sir-n-output").textContent = sirInputs.n.value;
    $("sir-initial-output").textContent = sirInputs.initial.value;
    $("sir-p-output").textContent = Number(sirInputs.p.value).toFixed(2);
    $("sir-q-output").textContent = Number(sirInputs.q.value).toFixed(2);
    $("sir-speed-output").textContent = `${sirInputs.speed.value} steps/s`;
  }

  function countSir(states = sirState.states) {
    const counts = { s: 0, i: 0, r: 0 };
    states.forEach((state) => {
      if (state === "S") counts.s += 1;
      else if (state === "I") counts.i += 1;
      else counts.r += 1;
    });
    return counts;
  }

  function drawSir(highlightStrength = 0) {
    const width = sirCanvas.width;
    const height = sirCanvas.height;
    const centreX = width / 2;
    const centreY = height / 2;
    const ringRadius = Math.min(width, height) * 0.37;
    const particleRadius = clamp(360 / Math.max(1, sirState.states.length), 7, 16);
    const colours = { S: "#218c68", I: "#df6658", R: "#2767b2" };

    clearCanvas(sirContext, sirCanvas);
    sirContext.strokeStyle = "#cbd6e3";
    sirContext.lineWidth = 2;
    sirContext.beginPath();
    sirContext.arc(centreX, centreY, ringRadius, 0, Math.PI * 2);
    sirContext.stroke();

    sirState.states.forEach((state, index) => {
      const angle = -Math.PI / 2 + (index * Math.PI * 2) / sirState.states.length;
      const x = centreX + Math.cos(angle) * ringRadius;
      const y = centreY + Math.sin(angle) * ringRadius;

      if (highlightStrength > 0 && sirState.changed.includes(index)) {
        sirContext.beginPath();
        sirContext.arc(x, y, particleRadius + 5 + 4 * highlightStrength, 0, Math.PI * 2);
        sirContext.strokeStyle = `rgba(244, 201, 93, ${highlightStrength})`;
        sirContext.lineWidth = 4;
        sirContext.stroke();
      }

      sirContext.beginPath();
      sirContext.arc(x, y, particleRadius, 0, Math.PI * 2);
      sirContext.fillStyle = colours[state];
      sirContext.fill();
      sirContext.strokeStyle = "#ffffff";
      sirContext.lineWidth = 2;
      sirContext.stroke();
      sirContext.fillStyle = "#ffffff";
      sirContext.font = `800 ${Math.max(8, particleRadius * 0.9)}px system-ui`;
      sirContext.textAlign = "center";
      sirContext.textBaseline = "middle";
      sirContext.fillText(state, x, y + 0.5);
    });

    const counts = countSir();
    sirContext.textAlign = "center";
    sirContext.textBaseline = "alphabetic";
    sirContext.fillStyle = "#17365d";
    sirContext.font = "800 32px system-ui";
    sirContext.fillText(`t = ${sirState.time}`, centreX, centreY - 13);
    sirContext.font = "700 18px system-ui";
    sirContext.fillText(`S ${counts.s}   I ${counts.i}   R ${counts.r}`, centreX, centreY + 24);
  }

  function animateSirChanges() {
    if (sirState.animationFrame !== null) cancelAnimationFrame(sirState.animationFrame);
    if (reducedMotion.matches || sirState.changed.length === 0) {
      drawSir();
      return;
    }
    const started = performance.now();
    const duration = 280;
    const frame = (now) => {
      const progress = clamp((now - started) / duration, 0, 1);
      drawSir(1 - progress);
      if (progress < 1) sirState.animationFrame = requestAnimationFrame(frame);
      else sirState.animationFrame = null;
    };
    sirState.animationFrame = requestAnimationFrame(frame);
  }

  function drawSirGraph() {
    const frame = drawGraphFrame(
      sirGraphContext,
      sirGraph,
      { left: 58, top: 34, right: 24, bottom: 50 },
      "Time, t",
      "Particle count"
    );
    const population = Math.max(1, sirState.states.length);
    const maximumTime = Math.max(1, sirState.time);
    const xFor = (time) => frame.left + (time / maximumTime) * frame.plotWidth;
    const yFor = (count) => frame.top + ((population - count) / population) * frame.plotHeight;

    sirGraphContext.font = "12px system-ui";
    sirGraphContext.fillStyle = "#607086";
    sirGraphContext.textAlign = "right";
    [0, 0.25, 0.5, 0.75, 1].forEach((fraction) => {
      const count = Math.round(population * fraction);
      const y = yFor(count);
      sirGraphContext.fillText(String(count), frame.left - 8, y + 4);
      sirGraphContext.strokeStyle = "#edf1f6";
      sirGraphContext.beginPath();
      sirGraphContext.moveTo(frame.left, y);
      sirGraphContext.lineTo(frame.left + frame.plotWidth, y);
      sirGraphContext.stroke();
    });

    const tickCount = Math.min(5, maximumTime);
    sirGraphContext.textAlign = "center";
    for (let tick = 0; tick <= tickCount; tick += 1) {
      const time = Math.round((tick / tickCount) * maximumTime);
      sirGraphContext.fillText(String(time), xFor(time), frame.top + frame.plotHeight + 19);
    }

    const series = [
      { key: "s", label: "S", colour: "#218c68" },
      { key: "i", label: "I", colour: "#df6658" },
      { key: "r", label: "R", colour: "#2767b2" }
    ];

    series.forEach((seriesItem, index) => {
      sirGraphContext.strokeStyle = seriesItem.colour;
      sirGraphContext.lineWidth = 3;
      sirGraphContext.lineJoin = "round";
      sirGraphContext.beginPath();
      sirState.history.forEach((entry, entryIndex) => {
        const x = xFor(entry.t);
        const y = yFor(entry[seriesItem.key]);
        if (entryIndex === 0) sirGraphContext.moveTo(x, y);
        else sirGraphContext.lineTo(x, y);
      });
      sirGraphContext.stroke();

      const legendX = frame.left + 12 + index * 58;
      sirGraphContext.fillStyle = seriesItem.colour;
      sirGraphContext.fillRect(legendX, 12, 17, 4);
      sirGraphContext.font = "700 12px system-ui";
      sirGraphContext.textAlign = "left";
      sirGraphContext.fillText(seriesItem.label, legendX + 22, 17);
    });
  }

  function updateSir(status) {
    const counts = countSir();
    $("sir-time").textContent = String(sirState.time);
    $("sir-s").textContent = String(counts.s);
    $("sir-i").textContent = String(counts.i);
    $("sir-r").textContent = String(counts.r);
    $("sir-peak").textContent = String(sirState.peak);
    $("sir-peak-time").textContent = String(sirState.peakTime);
    $("sir-duration").textContent = sirState.duration === null
      ? "Not yet ended"
      : `${sirState.duration} ${sirState.duration === 1 ? "step" : "steps"}`;
    $("sir-status").textContent = status;
    drawSirGraph();
    animateSirChanges();
    const ended = counts.i === 0;
    $("sir-step").disabled = ended;
    $("sir-run").disabled = ended || sirState.timer !== null;
  }

  function pauseSir(status = "Paused") {
    if (sirState.timer !== null) {
      window.clearInterval(sirState.timer);
      sirState.timer = null;
    }
    $("sir-pause").disabled = true;
    $("sir-run").disabled = countSir().i === 0;
    if (sirState.history.length > 0 && status) $("sir-status").textContent = status;
  }

  function sirStep() {
    const countsBefore = countSir();
    if (countsBefore.i === 0) {
      pauseSir("Epidemic ended");
      return;
    }

    const { p, q } = sirParameters();
    const previous = sirState.states;
    const next = previous.slice();
    const changed = [];

    previous.forEach((state, index) => {
      if (state === "S") {
        const leftInfected = previous[(index - 1 + previous.length) % previous.length] === "I" ? 1 : 0;
        const rightInfected = previous[(index + 1) % previous.length] === "I" ? 1 : 0;
        const infectedNeighbours = leftInfected + rightInfected;
        const infectionProbability = 1 - (1 - p) ** infectedNeighbours;
        if (infectedNeighbours > 0 && sirState.random() < infectionProbability) next[index] = "I";
      } else if (state === "I" && sirState.random() < q) {
        next[index] = "R";
      }
      if (next[index] !== state) changed.push(index);
    });

    sirState.states = next;
    sirState.time += 1;
    sirState.changed = changed;
    const counts = countSir();
    if (counts.i > sirState.peak) {
      sirState.peak = counts.i;
      sirState.peakTime = sirState.time;
    }
    if (counts.i === 0 && sirState.duration === null) sirState.duration = sirState.time;
    sirState.history.push({ t: sirState.time, ...counts });
    updateSir(counts.i === 0 ? "Epidemic ended" : sirState.timer === null ? "Advanced one step" : "Running");
    if (counts.i === 0) pauseSir("Epidemic ended");
  }

  function runSir() {
    if (sirState.timer !== null || countSir().i === 0) return;
    $("sir-run").disabled = true;
    $("sir-pause").disabled = false;
    $("sir-status").textContent = "Running";
    const delay = 1000 / Number(sirInputs.speed.value);
    sirState.timer = window.setInterval(sirStep, delay);
  }

  function resetSir() {
    pauseSir("");
    if (sirState.animationFrame !== null) {
      cancelAnimationFrame(sirState.animationFrame);
      sirState.animationFrame = null;
    }
    updateSirLabels();
    const parameters = sirParameters();
    sirState.seed = cleanSeed(sirInputs.seed);
    sirState.random = seededRandom(sirState.seed);
    sirState.states = Array(parameters.n).fill("S");

    const indices = Array.from({ length: parameters.n }, (_, index) => index);
    for (let index = 0; index < parameters.initial; index += 1) {
      const selected = index + Math.floor(sirState.random() * (parameters.n - index));
      [indices[index], indices[selected]] = [indices[selected], indices[index]];
      sirState.states[indices[index]] = "I";
    }

    sirState.time = 0;
    sirState.peak = parameters.initial;
    sirState.peakTime = 0;
    sirState.duration = null;
    sirState.changed = [];
    const counts = countSir();
    sirState.history = [{ t: 0, ...counts }];
    updateSir("Ready to run");
  }

  [sirInputs.n, sirInputs.initial, sirInputs.p, sirInputs.q].forEach((input) => {
    input.addEventListener("input", updateSirLabels);
    input.addEventListener("change", resetSir);
  });
  sirInputs.speed.addEventListener("input", updateSirLabels);
  sirInputs.speed.addEventListener("change", () => {
    if (sirState.timer !== null) {
      pauseSir("");
      runSir();
    }
  });
  $("sir-step").addEventListener("click", sirStep);
  $("sir-run").addEventListener("click", runSir);
  $("sir-pause").addEventListener("click", () => pauseSir());
  $("sir-reset").addEventListener("click", resetSir);
  $("sir-new-seed").addEventListener("click", () => {
    sirInputs.seed.value = createSeed();
    resetSir();
  });
  $("sir-download").addEventListener("click", () => {
    const parameters = sirParameters();
    const rows = [["t", "S", "I", "R", "N", "initial_infected", "p", "q", "seed"]];
    sirState.history.forEach((entry) => rows.push([
      entry.t,
      entry.s,
      entry.i,
      entry.r,
      parameters.n,
      parameters.initial,
      parameters.p.toFixed(2),
      parameters.q.toFixed(2),
      sirState.seed
    ]));
    downloadCsv(`scim211-sir-seed-${sirState.seed}.csv`, rows);
    announceCopy($("sir-copy-status"), `CSV prepared with ${rows.length - 1} time row${rows.length === 2 ? "" : "s"}.`);
  });
  $("sir-copy").addEventListener("click", async () => {
    const parameters = sirParameters();
    const counts = countSir();
    const summary = [
      "SCIM211 interacting-particle SIR experiment",
      `Seed: ${sirState.seed}`,
      `Parameters: N=${parameters.n}, initial infected=${parameters.initial}, p=${parameters.p.toFixed(2)}, q=${parameters.q.toFixed(2)}`,
      `Current result: t=${sirState.time}, S=${counts.s}, I=${counts.i}, R=${counts.r}`,
      `Peak infected: ${sirState.peak} at t=${sirState.peakTime}`,
      `Epidemic duration: ${sirState.duration === null ? "not yet ended" : `${sirState.duration} ${sirState.duration === 1 ? "step" : "steps"}`}`,
      "Update rule: susceptible infection probability = 1-(1-p)^k; infected recovery probability = q; updates are synchronous."
    ].join("\n");
    try {
      await copyText(summary);
      announceCopy($("sir-copy-status"), "Experiment summary copied.");
    } catch {
      announceCopy($("sir-copy-status"), "Copy was unavailable in this browser.");
    }
  });

  window.addEventListener("resize", () => {
    drawPi();
    drawPiGraph();
    drawSir();
    drawSirGraph();
  });

  updatePiSpeedLabel();
  resetPi();
  resetSir();
})();
