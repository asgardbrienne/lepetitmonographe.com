// Menu mobile, retour en haut de page, recherche et filtres de la page « Tous les dossiers ».
(function () {
  var bouton = document.querySelector('.bouton-menu');
  var nav = document.getElementById('menu-principal');
  if (bouton && nav) {
    document.documentElement.classList.add('js');
    bouton.addEventListener('click', function () {
      var ouvert = bouton.getAttribute('aria-expanded') === 'true';
      bouton.setAttribute('aria-expanded', String(!ouvert));
      nav.classList.toggle('ouvert', !ouvert);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('ouvert')) {
        bouton.setAttribute('aria-expanded', 'false');
        nav.classList.remove('ouvert');
        bouton.focus();
      }
    });
  }

  // Apparence claire ou sombre, mémorisée sur cet appareil
  Array.prototype.forEach.call(document.querySelectorAll('.bouton-theme'), function (theme) {
    theme.addEventListener('click', function () {
      var racine = document.documentElement;
      var sombre = racine.getAttribute('data-theme') === 'dark';
      var nouveau = sombre ? 'light' : 'dark';
      racine.setAttribute('data-theme', nouveau);
      try { localStorage.setItem('lpm-theme', nouveau); } catch (e) {}
    });
  });

  // Rubriques : le menu déroulant se ferme au clic extérieur et avec Échap
  var deroulants = document.querySelectorAll('.nav-deroulant details');
  document.addEventListener('click', function (e) {
    Array.prototype.forEach.call(deroulants, function (d) { if (!d.contains(e.target)) d.removeAttribute('open'); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') Array.prototype.forEach.call(deroulants, function (d) { d.removeAttribute('open'); });
  });

  // Accueil : enquêtes à la une (défilement manuel, sans lecture automatique)
  var diapos = document.getElementById('une-diapos');
  if (diapos) {
    var points = Array.prototype.slice.call(document.querySelectorAll('.une-point'));
    points.forEach(function (p) {
      p.addEventListener('click', function () {
        var cible = document.getElementById(p.getAttribute('data-cible'));
        diapos.scrollTo({ left: cible.offsetLeft, behavior: 'smooth' });
      });
    });
    var majPoints = function () {
      var n = Math.round(diapos.scrollLeft / diapos.clientWidth);
      points.forEach(function (p, i) { if (i === n) p.setAttribute('aria-current', 'true'); else p.removeAttribute('aria-current'); });
    };
    diapos.addEventListener('scroll', function () { window.requestAnimationFrame(majPoints); }, { passive: true });
  }

  // Rubriques : tri de la liste
  Array.prototype.forEach.call(document.querySelectorAll('[data-tri]'), function (sel) {
    var liste = document.getElementById(sel.getAttribute('data-tri'));
    sel.addEventListener('change', function () {
      var cle = sel.value;
      var items = Array.prototype.slice.call(liste.children);
      items.sort(function (a, b) {
        if (cle === 'titre') return a.getAttribute('data-titre').localeCompare(b.getAttribute('data-titre'), 'fr');
        if (cle === 'min') return (+a.getAttribute('data-min')) - (+b.getAttribute('data-min'));
        return (+a.getAttribute('data-ordre')) - (+b.getAttribute('data-ordre'));
      });
      items.forEach(function (i) { liste.appendChild(i); });
    });
  });

  // Dossier : enregistrer en PDF (impression) et partager
  Array.prototype.forEach.call(document.querySelectorAll('[data-action]'), function (b) {
    b.addEventListener('click', function () {
      if (b.getAttribute('data-action') === 'imprimer') { window.print(); return; }
      var url = window.location.href.split('#')[0];
      if (b.getAttribute('data-action') === 'copier') {
        if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () {
          b.classList.add('copie'); b.setAttribute('aria-label', 'Lien copié');
          setTimeout(function () { b.classList.remove('copie'); b.setAttribute('aria-label', 'Copier le lien du dossier'); }, 2000);
        });
        return;
      }
      if (navigator.share) { navigator.share({ title: document.title, url: url }).catch(function () {}); return; }
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function () {
          b.classList.add('copie');
          setTimeout(function () { b.classList.remove('copie'); }, 2000);
        });
      }
    });
  });

  var haut = document.querySelector('.haut-de-page');
  if (haut) {
    var maj = function () { haut.classList.toggle('visible', window.scrollY > 900); };
    window.addEventListener('scroll', maj, { passive: true });
    maj();
  }


  var champ = document.getElementById('champ-recherche');
  var liste = document.getElementById('liste-dossiers');
  if (!champ || !liste) return;
  var cartes = Array.prototype.slice.call(liste.querySelectorAll('[data-texte]'));
  var filtres = Array.prototype.slice.call(document.querySelectorAll('.filtre'));
  var compteur = document.getElementById('nb-resultats');
  var vide = document.getElementById('aucun-resultat');
  var rubrique = 'tous';
  var index = null, chargement = null;

  function sansAccents(t) {
    return t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }
  // Texte intégral des dossiers : chargé une seule fois, à la première recherche.
  function charger() {
    if (chargement) return;
    chargement = fetch('assets/recherche.json').then(function (r) { return r.json(); }).then(function (j) {
      index = {};
      Object.keys(j).forEach(function (k) { index[k] = sansAccents(j[k]); });
      appliquer();
    }).catch(function () { chargement = null; });
  }
  function appliquer() {
    var mots = sansAccents(champ.value.trim()).split(/\s+/).filter(Boolean);
    var n = 0;
    cartes.forEach(function (c) {
      var texte = sansAccents(c.getAttribute('data-texte') || '') +
        (index ? ' ' + (index[c.getAttribute('data-fichier')] || '') : '');
      var ok = (rubrique === 'tous' || c.getAttribute('data-rubrique') === rubrique) &&
        mots.every(function (m) { return texte.indexOf(m) !== -1; });
      c.hidden = !ok;
      if (ok) n++;
    });
    compteur.textContent = n;
    vide.hidden = n !== 0;
  }
  champ.addEventListener('focus', charger);
  champ.addEventListener('input', function () { charger(); appliquer(); });
  var q = new URLSearchParams(window.location.search).get('q');
  if (q) { champ.value = q; charger(); appliquer(); }
  filtres.forEach(function (f) {
    f.addEventListener('click', function () {
      rubrique = f.getAttribute('data-filtre');
      filtres.forEach(function (g) { g.setAttribute('aria-pressed', String(g === f)); });
      appliquer();
    });
  });
  if (location.hash === '#recherche') champ.focus();
})();
