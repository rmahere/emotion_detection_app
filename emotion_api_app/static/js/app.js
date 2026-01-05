async function postJSON(url, data) {
  const res = await fetch(url, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  const payload = await res.json().catch(() => ({}));
  if (!res.ok) {
    const msg = payload.error || `Request failed (${res.status})`;
    const details = payload.details ? ` Details: ${payload.details}` : "";
    throw new Error(msg + details);
  }
  return payload;
}

function prettyScores(scoresObj) {
  const lines = [];
  for (const [k, v] of Object.entries(scoresObj || {})) {
    lines.push(`${k}: ${v.toFixed(4)}`);
  }
  return lines.length ? lines.join("\n") : "—";
}

const els = {
  text: document.getElementById("text"),
  analyzeBtn: document.getElementById("analyzeBtn"),
  clearBtn: document.getElementById("clearBtn"),
  status: document.getElementById("status"),
  dominant: document.getElementById("dominant"),
  model: document.getElementById("model"),
  scores: document.getElementById("scores"),
};

function setStatus(msg, isError=false) {
  els.status.textContent = msg || "";
  els.status.className = "status" + (isError ? " error" : "");
}

async function analyze() {
  const text = (els.text.value || "").trim();
  if (!text) {
    setStatus("Please enter some text.", true);
    return;
  }
  setStatus("Analyzing…");
  els.analyzeBtn.disabled = true;

  try {
    const data = await postJSON("/api/analyze", {text});
    els.dominant.textContent = data.dominant_emotion || "—";
    els.model.textContent = data.model || "—";
    els.scores.textContent = prettyScores(data.scores);
    setStatus("");
  } catch (err) {
    setStatus(err.message || "Something went wrong.", true);
  } finally {
    els.analyzeBtn.disabled = false;
  }
}

function clearAll() {
  els.text.value = "";
  els.dominant.textContent = "—";
  els.model.textContent = "—";
  els.scores.textContent = "—";
  setStatus("");
}

els.analyzeBtn.addEventListener("click", analyze);
els.clearBtn.addEventListener("click", clearAll);
