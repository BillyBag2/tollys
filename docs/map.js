/* Location from the OpenStreetMap link in ABOUT-TOLLYS.md.
   A fixed location and permanent label avoid search-result positioning and popup auto-panning. */
(() => {
  const container = document.getElementById('cafe-map');
  if (!container || !window.L) return;

  container.querySelector('.map-fallback')?.remove();
  const location = [51.947765, -2.060414];
  const map = L.map(container, { scrollWheelZoom: false }).setView(location, 18);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  const icon = L.divIcon({
    className: 'cafe-pin',
    html: '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="60" viewBox="0 0 48 60" aria-hidden="true"><path d="M24 57C20 49 4 34 4 24a20 20 0 1 1 40 0c0 10-16 25-20 33Z" fill="#b84024" stroke="#fff" stroke-width="3"/><circle cx="24" cy="24" r="8" fill="#fff"/></svg>',
    iconSize: [48, 60],
    iconAnchor: [24, 57],
    tooltipAnchor: [0, -57]
  });
  L.marker(location, { icon, title: "Tolly's Cafe", alt: "Tolly's Cafe at Tarlings Yard" })
    .addTo(map)
    .bindTooltip("Tolly's", { permanent: true, direction: 'top', className: 'cafe-map-label', offset: [0, -8] });

  const centre = () => {
    map.invalidateSize({ pan: false });
    map.setView(location, 18, { animate: false });
  };
  const button = document.querySelector('.map-recentre');
  button.hidden = false;
  button.addEventListener('click', centre);
  // Recalculate after responsive layout and browser back/forward restoration.
  if (window.ResizeObserver) new ResizeObserver(centre).observe(container);
  window.addEventListener('pageshow', centre);
  centre();
})();
