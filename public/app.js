"use strict";
const ids = ["rain24", "rain7", "slope"];
const defaults = [42, 135, 32];
const nodes = ids.map(id => document.getElementById(id));
const outputs = ids.map(id => document.getElementById(id + "Value"));
const scoreNode = document.getElementById("score");
const bar = document.getElementById("meterFill");
const chart = document.getElementById("chart");

function update() {
  const rain24 = Number(nodes[0].value);
  const rain7 = Math.max(rain24, Number(nodes[1].value));
  if (rain7 !== Number(nodes[1].value)) nodes[1].value = String(rain7);
  const slope = Number(nodes[2].value);
  outputs[0].textContent = rain24 + " mm";
  outputs[1].textContent = rain7 + " mm";
  outputs[2].textContent = slope + "°";
  // Illustrative mathematical mapping only. These coefficients are invented,
  // unrelated to observed landslide frequency and never risk probabilities.
  const z = -5 + 0.035 * rain24 + 0.012 * rain7 + 0.04 * slope;
  const index = Math.round(100 / (1 + Math.exp(-z)));
  scoreNode.innerHTML = index + "<span>%</span>";
  bar.style.width = index + "%";
  renderChart(rain24, rain7);
}
function renderChart(rain24, rain7) {
  const series = Array.from({ length: 12 }, (_, i) =>
    Math.max(0, rain24 * (0.28 + (Math.sin(i * 1.53 + 1.2) + 1) * 0.28) + rain7 * 0.075 * (1 + Math.cos(i * 0.72)))
  );
  const maximum = Math.max(1, ...series) * 1.15;
  const left = 47, top = 16, width = 822, bottom = 187;
  const h = bottom - top;
  const points = series.map((v, i) => [left + i * width / 11, bottom - v / maximum * h]);
  const path = points.map(([x,y], i) => (i ? "L" : "M") + x.toFixed(1) + "," + y.toFixed(1)).join(" ");
  let html = "";
  for (let n = 0; n <= 4; n++) {
    const y = top + h * n / 4;
    html += '<line x1="' + left + '" y1="' + y + '" x2="869" y2="' + y + '" stroke="#49666c" stroke-opacity=".55" stroke-dasharray="4 7"/>';
    html += '<text x="35" y="' + (y + 4) + '" fill="#9bbab6" text-anchor="end" font-size="12">' + Math.round(maximum * (4-n)/4) + '</text>';
  }
  html += '<path d="' + path + '" fill="none" stroke="#a6eac2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>';
  for (const [x,y] of points) html += '<circle cx="' + x + '" cy="' + y + '" r="4" fill="#baf7cb" stroke="#12343a" stroke-width="2"/>';
  points.forEach(([x],i) => { if(i%2===0) html += '<text x="' + x + '" y="207" fill="#88aaa6" text-anchor="middle" font-size="12">P' + (i+1) + '</text>'; });
  chart.innerHTML = html;
}
nodes.forEach(node => node.addEventListener("input", update));
document.getElementById("reset").addEventListener("click", () => {
  nodes.forEach((node, i) => { node.value = String(defaults[i]); });
  update();
});
update();

// Reference basemap only: no hazard layers, observations, or predictions are implied.
function initializeReferenceMap() {
  const mapElement = document.getElementById("map");
  const status = document.getElementById("map-status");
  if (!mapElement || !status) return;
  const placeholder = mapElement.querySelector(".map-placeholder");
  if (typeof L === "undefined") {
    document.querySelectorAll("[data-map-view]").forEach(button => { button.disabled = true; });
    status.textContent = "No se pudo cargar el mapa. Comprueba tu conexión e inténtalo de nuevo.";
    status.dataset.state = "error";
    return;
  }

  const map = L.map(mapElement, { scrollWheelZoom: false }).setView([-16.7, -64.7], 5);
  const tiles = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>'
  });
  let loaded = false;
  tiles.on("tileload", () => {
    loaded = true;
    if (placeholder) placeholder.hidden = true;
    status.textContent = "Mapa base de referencia · sin capas científicas conectadas";
    status.dataset.state = "ready";
  });
  tiles.on("tileerror", () => {
    if (!loaded) {
      status.textContent = "No se pudieron cargar los mosaicos del mapa. Comprueba tu conexión.";
      status.dataset.state = "error";
    }
  });
  tiles.addTo(map);
  document.querySelectorAll("[data-map-view]").forEach(button => {
    button.addEventListener("click", () => {
      const isLaPaz = button.dataset.mapView === "lapaz";
      map.setView(isLaPaz ? [-16.5, -68.15] : [-16.7, -64.7], isLaPaz ? 11 : 5);
      document.querySelectorAll("[data-map-view]").forEach(item => {
        item.setAttribute("aria-pressed", String(item === button));
      });
    });
  });
}
initializeReferenceMap();

