// ── Language ──
let lang = "pt";

function toggleLang() {
  lang = lang === "pt" ? "en" : "pt";
  document.querySelectorAll("[data-pt]").forEach(el => {
    el.textContent = el.dataset[lang];
  });
  document.getElementById("langBtn").textContent = lang === "pt" ? "EN" : "PT";
}

// ── Pills ──
function selectPill(el) {
  document.querySelectorAll(".pill").forEach((b) => b.classList.remove("active"));
  el.classList.add("active");
}

// ── Download ──
function handleDownload() {
  const url = document.getElementById("urlInput").value.trim();
  const fmt = document.querySelector(".pill.active").textContent;
  const status = document.getElementById("statusText");

  if (!url) {
    status.textContent = lang === "pt"
      ? "Cole uma URL válida primeiro."
      : "Please paste a valid URL first.";
    return;
  }

  status.textContent = lang === "pt"
    ? `Processando ${fmt}... (backend não conectado ainda)`
    : `Processing ${fmt}... (backend not connected yet)`;

  // ALL: connect to the backend FastAPI
  // fetch("/api/download", {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify({ url, format: fmt })
  // })
}