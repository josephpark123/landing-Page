/* Prebuilt airports: download only the airport the visitor chooses. */
(() => {
  'use strict';
  // BEGIN GENERATED ASSET VERSIONS — scripts/refresh_airport_catalog.py
  const assetVersions = {"RKSI":{"airport-scene.glb":"2f39fa65873ef911","scene.json":"af5cdaf857c87871","replay.bin":"9eeadab6b9ae1029"},"RPLL":{"airport-scene.glb":"e8a5a06d5ca29872","scene.json":"d7bf215d3dd05fac","replay.bin":"f0e853d89ad7e172"},"RJAA":{"airport-scene.glb":"a01813cc2c61f6d7","scene.json":"05339281e208f5c0","replay.bin":"6b4874e079117567"},"VTBS":{"airport-scene.glb":"5baaeeaff9dcfcb3","scene.json":"1b5db90bda4688ae","replay.bin":"a16d497d29f588aa"},"VVTS":{"airport-scene.glb":"0876504568f152a7","scene.json":"01387954ee7c9f59","replay.bin":"8beabc329dc79015"},"LOWW":{"airport-scene.glb":"0f2cb889e5a3a7dd","scene.json":"57f917ae22cb2d04","replay.bin":"d983405c380a205d"}};
  // END GENERATED ASSET VERSIONS
  const base = new URL('.', document.currentScript.src);
  const stylesheet = document.createElement('link');
  stylesheet.rel = 'stylesheet';
  stylesheet.href = new URL('airports.css?v=mobile-picker-1', base);
  document.head.appendChild(stylesheet);
  const host = document.querySelector('.location');
  if (!host) return;
  const presets = [
    ['RKSI', 'ICN', 'Incheon', 'South Korea'], ['RPLL', 'MNL', 'Manila', 'Philippines'],
    ['VTBS', 'BKK', 'Bangkok', 'Thailand'], ['RJAA', 'NRT', 'Narita', 'Japan'],
    ['VVTS', 'SGN', 'Ho Chi Minh', 'Vietnam'], ['LOWW', 'VIE', 'Vienna', 'Austria']
  ];
  const requested = (new URLSearchParams(location.search).get('airport') || 'RKSI').trim().toUpperCase();
  let current = presets.find(p => p[0] === requested || p[1] === requested)?.[0] || 'RKSI';
  let open = false, busy = false;
  host.className = 'location airport-location';
  host.innerHTML = `<button type="button" class="airport-select" role="combobox" aria-label="Airport" aria-haspopup="listbox" aria-expanded="false" aria-controls="airport-options">
    <span class="airport-current-code" aria-hidden="true"></span><span class="airport-current-copy"><span class="airport-caption">Explore airport</span><span class="airport-current-name"></span></span>
    <svg class="airport-chevron" viewBox="0 0 20 20" aria-hidden="true"><path d="m6 8 4 4 4-4"/></svg></button>
    <div class="airport-backdrop" hidden></div>
    <div class="airport-panel" hidden><div class="airport-panel-heading"><span>Choose an airport</span><button type="button" class="airport-close" aria-label="Close airport selection"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="m6 6 8 8M14 6l-8 8"/></svg></button></div><div id="airport-options" role="listbox" aria-label="Airports"></div></div>
    <p class="airport-inline-status" role="status" hidden></p>`;
  const picker = host.querySelector('.airport-select'), panel = host.querySelector('.airport-panel');
  const backdrop = host.querySelector('.airport-backdrop'), list = host.querySelector('[role="listbox"]');
  const status = host.querySelector('.airport-inline-status'), closeButton = host.querySelector('.airport-close');
  const options = presets.map(([code, iata, name, country]) => {
    const option = document.createElement('button');
    option.type = 'button'; option.className = 'airport-option'; option.setAttribute('role', 'option');
    option.dataset.code = code; option.tabIndex = -1;
    option.innerHTML = `<span class="airport-option-code">${iata}</span><span class="airport-option-copy"><span>${name}</span><small>${country}</small></span><svg class="airport-check" viewBox="0 0 20 20" aria-hidden="true"><path d="m5 10 3 3 7-7"/></svg>`;
    option.addEventListener('click', () => choose(code)); list.appendChild(option); return option;
  });
  function setCurrent(code) {
    const preset = presets.find(p => p[0] === code); if (!preset) return;
    current = code;
    host.querySelector('.airport-current-code').textContent = preset[1];
    host.querySelector('.airport-current-name').textContent = preset[2];
    picker.title = `${preset[2]} (${preset[0]})`;
    for (const option of options) option.setAttribute('aria-selected', String(option.dataset.code === code));
  }
  function setOpen(value, restoreFocus = true) {
    if (value && busy) return;
    open = value; panel.hidden = !value; backdrop.hidden = !value;
    picker.setAttribute('aria-expanded', String(value)); host.classList.toggle('is-open', value);
    if (value) options.find(o => o.dataset.code === current).focus({preventScroll: true});
    else if (restoreFocus && host.contains(document.activeElement)) picker.focus({preventScroll: true});
  }
  function setBusy(value) {
    if (value) setOpen(false);
    busy = Boolean(value); picker.disabled = busy; picker.setAttribute('aria-busy', String(busy));
    host.classList.toggle('is-busy', busy);
  }
  async function choose(code) {
    setOpen(false);
    if (busy || code === current) return;
    setBusy(true); status.hidden = true;
    try {
      try { sessionStorage.removeItem('restore-airport-view'); sessionStorage.removeItem('airport-selection-ready'); } catch (_) {}
      window.FlexaPageTransitions?.prepareAirportChange();
      if (window.airportMockup?.loadAirport) await window.airportMockup.loadAirport(code);
      else location.assign(code === 'RKSI' ? '/' : '/?airport=' + code);
    } catch (error) {
      setBusy(false); window.FlexaPageTransitions?.cancelAirportChange();
      status.textContent = 'Could not switch airports. Please try again.'; status.hidden = false;
      status.classList.add('error');
    }
  }
  picker.addEventListener('click', () => setOpen(!open));
  closeButton.addEventListener('click', () => setOpen(false));
  backdrop.addEventListener('click', () => setOpen(false));
  document.addEventListener('pointerdown', event => { if (open && !host.contains(event.target)) setOpen(false, false); });
  host.addEventListener('focusout', event => { if (open && event.relatedTarget && !host.contains(event.relatedTarget)) setOpen(false, false); });
  host.addEventListener('keydown', event => {
    if (event.key === 'Escape' && open) { event.preventDefault(); event.stopPropagation(); setOpen(false); return; }
    if (['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) {
      event.preventDefault(); const wasOpen = open;
      if (!open) setOpen(true);
      if (!open) return;
      let index = options.indexOf(document.activeElement);
      if (event.key === 'Home') index = 0;
      else if (event.key === 'End') index = options.length - 1;
      else if (wasOpen) index = (index + (event.key === 'ArrowDown' ? 1 : -1) + options.length) % options.length;
      options[Math.max(0, index)].focus({preventScroll: true});
    }
  });
  setCurrent(current);
  window.airportSelector = {setCurrent, setBusy};
  window.airportSelectionReady = Promise.resolve({icao: current, assetVersions: assetVersions[current], assetBase: current === 'RKSI' ? '/web/airport-mockup/' : '/web/airport-mockup/airports/' + current + '/'});
  window.addEventListener('airport-scene-ready', () => { const s = window.airportMockup?.getSnapshot(); if (s) setCurrent(s.icao); setBusy(false); });
  window.addEventListener('airport-scene-error', () => setBusy(false));
  window.addEventListener('pageshow', event => { if (event.persisted) { setBusy(false); setOpen(false, false); } });
})();
