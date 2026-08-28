// Play6x homepage logic
(function () {
  const grid = document.getElementById("gamesGrid");
  const emptyState = document.getElementById("emptyState");
  const searchInput = document.getElementById("searchInput");
  const categorySelect = document.getElementById("categorySelect");
  const sectionTabs = document.getElementById("sectionTabs");
  const resultsTitle = document.getElementById("resultsTitle");
  const resultsCount = document.getElementById("resultsCount");
  const statPlayable = document.getElementById("statPlayable");
  const statTotal = document.getElementById("statTotal");
  const headerStats = document.getElementById("headerStats");

  const GRADIENTS = [
    ["#7c5cff", "#22d3ee"],
    ["#ff4d8d", "#7c5cff"],
    ["#22d3ee", "#34d399"],
    ["#f59e0b", "#ff4d8d"],
    ["#34d399", "#22d3ee"],
    ["#a855f7", "#22d3ee"],
    ["#ef4444", "#f59e0b"],
    ["#3b82f6", "#a855f7"],
  ];

  function hashStr(s) {
    let h = 0;
    for (let i = 0; i < s.length; i++) {
      h = (h * 31 + s.charCodeAt(i)) >>> 0;
    }
    return h;
  }

  function gradientFor(id) {
    const pair = GRADIENTS[hashStr(id) % GRADIENTS.length];
    return `linear-gradient(135deg, ${pair[0]}33, ${pair[1]}33)`;
  }

  let state = {
    section: "all",
    category: "all",
    query: "",
  };

  function populateCategories() {
    const cats = Array.from(new Set(GAMES.map((g) => g.category))).sort();
    for (const c of cats) {
      const opt = document.createElement("option");
      opt.value = c;
      opt.textContent = c;
      categorySelect.appendChild(opt);
    }
  }

  function matchesFilters(g) {
    if (state.section === "playable" && !g.playable) return false;
    if (state.section !== "all" && state.section !== "playable" && g.section !== state.section) return false;
    if (state.category !== "all" && g.category !== state.category) return false;
    if (state.query) {
      const q = state.query.toLowerCase();
      if (!g.name.toLowerCase().includes(q) && !g.category.toLowerCase().includes(q)) return false;
    }
    return true;
  }

  function cardHTML(g) {
    const pill = g.playable
      ? `<span class="play-pill">▶ PLAY NOW</span>`
      : `<span class="play-pill soon">SOON</span>`;
    return `
      <a class="game-card" href="play.html?id=${encodeURIComponent(g.id)}">
        <div class="game-thumb" style="background:${gradientFor(g.id)}">
          ${pill}
          <span>${g.icon}</span>
        </div>
        <div class="game-info">
          <h3>${g.name}</h3>
          <div class="game-cat">${g.category}</div>
        </div>
      </a>`;
  }

  function render() {
    const filtered = GAMES.filter(matchesFilters);
    grid.innerHTML = filtered.map(cardHTML).join("");
    emptyState.style.display = filtered.length ? "none" : "block";
    resultsCount.textContent = `${filtered.length} game${filtered.length === 1 ? "" : "s"}`;

    const titles = {
      all: "All Games",
      playable: "Playable Now",
      Original: "Play6x Originals",
      Main: "Main Games",
      Driving: "Driving Games",
      Flash: "Flash Games",
    };
    resultsTitle.textContent = titles[state.section] || "Games";
  }

  sectionTabs.addEventListener("click", (e) => {
    const btn = e.target.closest(".tab-btn");
    if (!btn) return;
    sectionTabs.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    state.section = btn.dataset.section;
    render();
  });

  categorySelect.addEventListener("change", () => {
    state.category = categorySelect.value;
    render();
  });

  let searchDebounce;
  searchInput.addEventListener("input", () => {
    clearTimeout(searchDebounce);
    searchDebounce = setTimeout(() => {
      state.query = searchInput.value.trim();
      render();
    }, 120);
  });

  function init() {
    populateCategories();
    const params = new URLSearchParams(window.location.search);
    const q = params.get("q");
    if (q) {
      searchInput.value = q;
      state.query = q;
    }
    const total = GAMES.length;
    const playable = GAMES.filter((g) => g.playable).length;
    statTotal.textContent = total;
    statPlayable.textContent = playable;
    headerStats.textContent = `${playable} playable · ${total} catalogued`;
    render();
  }

  init();
})();
