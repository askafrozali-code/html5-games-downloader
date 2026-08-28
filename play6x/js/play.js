// Play6x game player page logic
(function () {
  const playTitle = document.getElementById("playTitle");
  const stageWrap = document.getElementById("stageWrap");
  const relatedGrid = document.getElementById("relatedGrid");
  const searchInput = document.getElementById("searchInput");

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
    for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0;
    return h;
  }

  function gradientFor(id) {
    const pair = GRADIENTS[hashStr(id) % GRADIENTS.length];
    return `linear-gradient(135deg, ${pair[0]}33, ${pair[1]}33)`;
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

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");
  const game = GAMES.find((g) => g.id === id) || GAMES[0];

  document.title = `${game.name} — Play6x`;

  playTitle.innerHTML = `
    <div class="icon-box" style="background:${gradientFor(game.id)}">${game.icon}</div>
    <div>
      <h1>${game.name}</h1>
      <div class="meta">${game.category} &middot; ${game.section === "Original" ? "Play6x Original" : game.section + " collection"}</div>
    </div>
  `;

  if (game.playable && game.path) {
    stageWrap.innerHTML = `
      <div class="game-stage">
        <iframe src="${game.path}" title="${game.name}" loading="lazy" allow="autoplay; fullscreen" allowfullscreen></iframe>
      </div>`;
  } else {
    stageWrap.innerHTML = `
      <div class="game-stage">
        <div class="coming-soon">
          <div class="big-icon">${game.icon}</div>
          <h2>${game.name} is coming soon</h2>
          <p>This title is catalogued from the Play6x game library but isn't playable in-browser yet.<br>
          Try one of our "Playable Now" originals below while we work on it.</p>
        </div>
      </div>`;
  }

  const related = GAMES.filter((g) => g.id !== game.id && g.category === game.category).slice(0, 12);
  const fallback = related.length
    ? related
    : GAMES.filter((g) => g.id !== game.id && g.playable).slice(0, 12);
  relatedGrid.innerHTML = fallback.map(cardHTML).join("");

  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && searchInput.value.trim()) {
      window.location.href = `index.html?q=${encodeURIComponent(searchInput.value.trim())}`;
    }
  });
})();
