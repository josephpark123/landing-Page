/* Sliding is reserved for Mock up <-> Solutions; airport changes stay put. */
(() => {
  'use strict';
  const mockupPaths = ['/', '/index.html', '/web/airport-mockup/', '/web/airport-mockup/index.html'];
  const isMockup = url => url.origin === location.origin && mockupPaths.includes(url.pathname);
  const mobile = /KAKAOTALK/i.test(navigator.userAgent) || matchMedia('(pointer: coarse)').matches || (navigator.maxTouchPoints > 0 && Math.min(screen.width, screen.height) <= 1024);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fallback = mobile || !('onpagereveal' in window);
  let leaving = false, airportChanging = false, leaveTimer;
  const read = key => { try { return JSON.parse(sessionStorage.getItem(key)); } catch (_) { return null; } };
  const write = (key, value) => { try { sessionStorage.setItem(key, JSON.stringify(value)); } catch (_) {} };
  const remove = key => { try { sessionStorage.removeItem(key); } catch (_) {} };
  function setNativeDisabled(disabled) {
    let style = document.getElementById('airport-transition-policy');
    if (disabled && !style) {
      style = document.createElement('style'); style.id = 'airport-transition-policy';
      style.textContent = '@view-transition { navigation: none; }'; document.head.appendChild(style);
    } else if (!disabled) style?.remove();
  }
  setNativeDisabled(fallback);
  function prepareAirportChange() {
    airportChanging = true; setNativeDisabled(true); remove('flexa-slide-entry');
    write('flexa-airport-change', {at: Date.now()});
    delete document.documentElement.dataset.slideEnter; delete document.documentElement.dataset.slideExit;
  }
  function cancelAirportChange() { airportChanging = false; remove('flexa-airport-change'); setNativeDisabled(fallback); }
  window.FlexaPageTransitions = {prepareAirportChange, cancelAirportChange};
  function revealFallback() {
    const entry = read('flexa-slide-entry'); remove('flexa-slide-entry');
    if (!entry || reduced || Date.now() - entry.at > 20000 || entry.target !== location.pathname + location.search) return;
    document.documentElement.dataset.slideEnter = entry.direction;
    const finish = () => delete document.documentElement.dataset.slideEnter;
    document.addEventListener('animationend', event => { if (event.target === document.body) finish(); }, {once: true});
    setTimeout(finish, 1100);
  }
  if (fallback) revealFallback();
  document.addEventListener('click', event => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('a.solutions-cta, a.mockup-return');
    if (!link) return;
    const returning = link.matches('.mockup-return');
    let destination = new URL(link.href);
    if (destination.origin !== location.origin) return;
    if (!returning) {
      const state = window.airportMockup?.getSnapshot();
      if (state) write('airport-view', state);
    } else {
      try { sessionStorage.setItem('restore-airport-view', 'true'); } catch (_) {}
      const code = read('airport-view')?.icao;
      if (['RKSI','RPLL','VTBS','RJAA','VVTS','LOWW'].includes(code)) destination = new URL(code === 'RKSI' ? '/' : '/?airport=' + code, location.origin);
    }
    cancelAirportChange();
    if (fallback) {
      event.preventDefault(); if (leaving) return;
      leaving = true;
      // Release the old decoder/context before another document starts loading.
      if (returning) window.flexaReleaseMedia?.();
      else window.airportMockup?.prepareNavigation({preserveState: true});
      const navigate = () => {
        if (!reduced) write('flexa-slide-entry', {direction: returning ? 'right' : 'left', target: destination.pathname + destination.search, at: Date.now()});
        location.assign(destination.href);
      };
      if (reduced) navigate();
      else { document.documentElement.dataset.slideExit = returning ? 'right' : 'left'; leaveTimer = setTimeout(navigate, 460); }
      return;
    }
    if (returning) {
      const navigation = window.navigation;
      const previous = navigation?.canGoBack && navigation.entries()[navigation.currentEntry.index - 1];
      if (previous && isMockup(new URL(previous.url))) { event.preventDefault(); history.back(); }
      else if (destination.href !== link.href) { event.preventDefault(); location.assign(destination.href); }
    }
  });
  window.addEventListener('pageswap', event => {
    const next = event.activation?.entry?.url;
    if (airportChanging || (document.documentElement.dataset.page === 'mockup' && next && isMockup(new URL(next)))) event.viewTransition?.skipTransition();
  });
  window.addEventListener('pagereveal', event => {
    if (!event.viewTransition) return;
    const from = window.navigation?.activation?.from?.url;
    const airportChange = read('flexa-airport-change'); remove('flexa-airport-change');
    if (fallback || (document.documentElement.dataset.page === 'mockup' && ((from && isMockup(new URL(from))) || (airportChange && Date.now() - airportChange.at < 20000)))) {
      event.viewTransition.skipTransition(); return;
    }
    if (document.documentElement.dataset.page === 'mockup' && !window.airportMockup?.getSnapshot().ready) {
      document.documentElement.dataset.slidePending = '';
      const resume = () => {
        clearTimeout(timeout);
        window.removeEventListener('airport-scene-ready', resume); window.removeEventListener('airport-scene-error', resume);
        const loader = document.getElementById('loader');
        if (loader?.classList.contains('loaded')) {
          loader.style.transition = 'none';
          const reset = () => loader.style.removeProperty('transition'); event.viewTransition.finished.then(reset, reset);
        }
        delete document.documentElement.dataset.slidePending;
      };
      const timeout = setTimeout(resume, 2500);
      window.addEventListener('airport-scene-ready', resume); window.addEventListener('airport-scene-error', resume);
    }
    for (const element of document.querySelectorAll('.reveal-up')) {
      const bounds = element.getBoundingClientRect();
      if (bounds.bottom > 0 && bounds.top < innerHeight) {
        element.style.transition = 'none'; element.classList.add('is-visible');
        const reset = () => element.style.removeProperty('transition'); event.viewTransition.finished.then(reset, reset);
      }
    }
  });
  window.addEventListener('pageshow', event => {
    if (!event.persisted) return;
    leaving = false; clearTimeout(leaveTimer); delete document.documentElement.dataset.slideExit;
    cancelAirportChange();
    if (event.persisted && fallback) revealFallback();
  });
})();
