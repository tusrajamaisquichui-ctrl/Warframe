/* Protea Prime guide: tabs with deep links, table of contents sheet, scroll spy. No dependencies.
   Without this script every panel stays visible and the tab bar works as plain anchor links. */
(function () {
  "use strict";

  var root = document.documentElement;
  var panels = [].slice.call(document.querySelectorAll(".panel"));
  var tabs = [].slice.call(document.querySelectorAll(".tab[data-tab]"));
  var tocToggle = document.querySelector(".toc-toggle");
  var backdrop = document.querySelector(".toc-backdrop");
  var toTop = document.querySelector(".to-top");
  var context = document.querySelector("[data-context]");
  var sheetQuery = window.matchMedia("(max-width: 1023.98px)");
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)");
  var untilFound = "onbeforematch" in document.body;
  var scrollMemory = {};
  var current = null;
  var spyHeads = [];
  var spyLinks = {};
  var spyActive = null;

  if (!panels.length) return;

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: calm.matches ? "auto" : "smooth" });
  }

  function hide(panel) {
    // hidden="until-found" keeps the text reachable by the browser's find-in-page.
    if (untilFound) panel.setAttribute("hidden", "until-found");
    else panel.hidden = true;
  }

  function activate(panel) {
    if (panel === current) return;
    if (current) scrollMemory[current.id] = window.scrollY;
    if (tabs.length) {
      panels.forEach(function (p) {
        if (p === panel) p.removeAttribute("hidden");
        else hide(p);
      });
      tabs.forEach(function (t) {
        var on = t.getAttribute("data-tab") === panel.id;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        t.classList.toggle("is-active", on);
      });
      if (panel.getAttribute("data-title")) document.title = panel.getAttribute("data-title");
      if (context && panel.getAttribute("data-label")) context.textContent = panel.getAttribute("data-label");
    }
    current = panel;
    closeToc(false);
    var toc = panel.querySelector(".toc");
    if (tocToggle) {
      tocToggle.hidden = !toc;
      if (toc) tocToggle.setAttribute("aria-controls", toc.id);
    }
    watch(panel);
    labelScrollers(panel);
  }

  function panelFor(el) {
    if (el.classList.contains("panel")) return el;
    return el.closest ? el.closest(".panel") : null;
  }

  // Show the panel that holds the URL fragment; restore that tab's scroll position.
  function route(initial) {
    var id = "";
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { id = ""; }
    var target = id ? document.getElementById(id) : null;
    var panel = target ? panelFor(target) : null;
    if (target && !panel) { // e.g. the skip link: keep the current tab
      if (!current) activate(panels[0]);
      return;
    }
    if (!panel) panel = current || panels[0];
    var changed = panel !== current;
    activate(panel);
    if (target && target !== panel) target.scrollIntoView({ block: "start" });
    else if (changed || initial) window.scrollTo(0, scrollMemory[panel.id] || 0);
  }

  // ---------- Tabs ----------

  if (tabs.length) {
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    var tablist = tabs[0].parentNode;
    tablist.setAttribute("role", "tablist");
    tabs.forEach(function (t) {
      var panel = document.getElementById(t.getAttribute("data-tab"));
      t.setAttribute("role", "tab");
      t.setAttribute("aria-controls", panel.id);
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("aria-labelledby", t.id);
      panel.removeAttribute("aria-label");
      t.addEventListener("click", function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button > 0) return;
        e.preventDefault();
        if (panel === current) {
          scrollToTop();
          return;
        }
        activate(panel);
        if (location.hash !== "#" + panel.id) history.pushState(null, "", "#" + panel.id);
        window.scrollTo(0, scrollMemory[panel.id] || 0);
      });
    });
    tablist.addEventListener("keydown", function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      var next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
      if (next === undefined) return;
      e.preventDefault();
      next = (next + tabs.length) % tabs.length;
      tabs[next].focus();
      tabs[next].click();
    });
    panels.forEach(function (p) {
      // Find-in-page matched text in a hidden tab: switch to it.
      p.addEventListener("beforematch", function () {
        activate(p);
        history.replaceState(null, "", "#" + p.id);
      });
    });
    window.addEventListener("popstate", function () { route(false); });
    window.addEventListener("hashchange", function () { route(false); });
  }

  // ---------- Table of contents: bottom sheet on phones ----------

  function openToc() {
    var toc = current && current.querySelector(".toc");
    if (!toc || !sheetQuery.matches) return;
    root.classList.add("toc-open");
    if (backdrop) backdrop.hidden = false;
    if (tocToggle) tocToggle.setAttribute("aria-expanded", "true");
    var link = toc.querySelector("a[aria-current]") || toc.querySelector("a");
    if (link) {
      link.focus({ preventScroll: true });
      toc.scrollTop = Math.max(0, link.offsetTop - toc.clientHeight / 2);
    }
  }

  function closeToc(returnFocus) {
    if (!root.classList.contains("toc-open")) return;
    root.classList.remove("toc-open");
    if (backdrop) backdrop.hidden = true;
    if (tocToggle) {
      tocToggle.setAttribute("aria-expanded", "false");
      if (returnFocus) tocToggle.focus();
    }
  }

  if (tocToggle) {
    tocToggle.addEventListener("click", function () {
      if (root.classList.contains("toc-open")) closeToc(true);
      else openToc();
    });
  }
  if (backdrop) backdrop.addEventListener("click", function () { closeToc(true); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeToc(true);
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest) return;
    if (e.target.closest(".toc-close")) closeToc(true);
    else if (e.target.closest(".toc a")) closeToc(false);
  });
  var onSheetChange = function () { if (!sheetQuery.matches) closeToc(false); };
  if (sheetQuery.addEventListener) sheetQuery.addEventListener("change", onSheetChange);
  else if (sheetQuery.addListener) sheetQuery.addListener(onSheetChange);

  // ---------- Scroll spy and back-to-top button ----------

  function watch(panel) {
    spyHeads = [];
    spyLinks = {};
    if (spyActive) spyActive.removeAttribute("aria-current");
    spyActive = null;
    var toc = panel.querySelector(".toc");
    if (toc) {
      [].forEach.call(toc.querySelectorAll('a[href^="#"]'), function (a) {
        spyLinks[a.getAttribute("href").slice(1)] = a;
      });
      spyHeads = [].filter.call(panel.querySelectorAll("h2[id], h3[id], h4[id]"), function (h) {
        return spyLinks[h.id];
      });
    }
    update();
  }

  function update() {
    if (toTop) toTop.classList.toggle("show", window.scrollY > 700);
    if (!spyHeads.length) return;
    var line = 96; // sticky bar (56 px) + margin
    var active = null;
    for (var i = 0; i < spyHeads.length; i++) {
      if (spyHeads[i].getBoundingClientRect().top <= line) active = spyHeads[i];
      else break;
    }
    var link = active ? spyLinks[active.id] : null;
    if (link === spyActive) return;
    if (spyActive) spyActive.removeAttribute("aria-current");
    spyActive = link;
    if (!link) return;
    link.setAttribute("aria-current", "location");
    var toc = link.closest(".toc");
    if (toc && !sheetQuery.matches && toc.scrollHeight > toc.clientHeight) {
      var top = link.offsetTop;
      if (top < toc.scrollTop + 40 || top > toc.scrollTop + toc.clientHeight - 60) {
        toc.scrollTop = top - toc.clientHeight / 3;
      }
    }
  }

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      ticking = false;
      update();
    });
  }, { passive: true });

  if (toTop) {
    toTop.hidden = false;
    toTop.addEventListener("click", scrollToTop);
  }

  // ---------- Wide tables: make the scrollable ones reachable from the keyboard ----------

  function labelScrollers(scope) {
    [].forEach.call(scope.querySelectorAll(".table-wrap"), function (w) {
      var scrolls = w.scrollWidth > w.clientWidth + 1;
      if (scrolls && !w.hasAttribute("tabindex")) {
        w.tabIndex = 0;
        w.setAttribute("role", "region");
        w.setAttribute("aria-label", "Tableau défilant horizontalement");
      } else if (!scrolls && w.hasAttribute("tabindex")) {
        w.removeAttribute("tabindex");
        w.removeAttribute("role");
        w.removeAttribute("aria-label");
      }
    });
  }

  var resizeTimer = null;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { if (current) labelScrollers(current); }, 200);
  });

  if (tabs.length) route(true);
  else activate(panels[0]);
  root.classList.add("ready");
})();
