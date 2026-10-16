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
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        bouton.setAttribute('aria-expanded', 'false');
        nav.classList.remove('ouvert');
      }
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
  var theme = document.querySelector('.bouton-theme');
  if (theme) {
    var racineTheme = document.documentElement;
    var initialementSombre = racineTheme.getAttribute('data-theme') === 'dark' ||
      (!racineTheme.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    theme.setAttribute('aria-pressed', String(initialementSombre));
    theme.addEventListener('click', function () {
      var racine = document.documentElement;
      var sombre = racine.getAttribute('data-theme') === 'dark' ||
        (!racine.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
      var nouveau = sombre ? 'light' : 'dark';
      racine.setAttribute('data-theme', nouveau);
      theme.setAttribute('aria-pressed', String(nouveau === 'dark'));
      try { localStorage.setItem('lpm-theme', nouveau); } catch (e) {}
    });
  }

  // Filtres « À la une » sur l'accueil
  var puces = Array.prototype.slice.call(document.querySelectorAll('.puce'));
  var une = document.getElementById('cartes-une');
  if (puces.length && une) {
    puces.forEach(function (p) {
      p.addEventListener('click', function () {
        var r = p.getAttribute('data-puce');
        puces.forEach(function (q) { q.setAttribute('aria-pressed', String(q === p)); });
        Array.prototype.forEach.call(une.querySelectorAll('.porte'), function (c) {
          c.hidden = r !== 'tous' && c.getAttribute('data-rubrique') !== r;
        });
      });
    });
  }

  var haut = document.querySelector('.haut-de-page');
  if (haut) {
    var maj = function () { haut.classList.toggle('visible', window.scrollY > 900); };
    window.addEventListener('scroll', maj, { passive: true });
    maj();
  }

  // Sommaire : fermé par défaut sur petit écran
  var sommaire = document.querySelector('.sommaire');
  if (sommaire && window.matchMedia('(max-width: 1039px)').matches) sommaire.removeAttribute('open');

  // Repère de lecture : suivre la section actuellement parcourue.
  // Les liens et identifiants sont ceux des sommaires déjà présents dans chaque dossier.
  var liensSommaire = Array.prototype.slice.call(
    document.querySelectorAll('.dossier .sommaire a[href^="#"]')
  );
  if (liensSommaire.length) {
    var etapesSommaire = liensSommaire.map(function (lien) {
      var identifiant = lien.getAttribute('href').slice(1);
      return { lien: lien, section: document.getElementById(identifiant) };
    }).filter(function (etape) { return !!etape.section; });
    if (etapesSommaire.length) {
      var defilementEnCours = false;
      function repererSection() {
        var active = etapesSommaire[0];
        etapesSommaire.forEach(function (etape) {
          if (etape.section.getBoundingClientRect().top <= 158) active = etape;
        });
        etapesSommaire.forEach(function (etape) {
          if (etape === active) etape.lien.setAttribute('aria-current', 'location');
          else etape.lien.removeAttribute('aria-current');
        });
        defilementEnCours = false;
      }
      window.addEventListener('scroll', function () {
        if (!defilementEnCours) {
          defilementEnCours = true;
          window.requestAnimationFrame(repererSection);
        }
      }, { passive: true });
      window.addEventListener('resize', repererSection);
      repererSection();
    }
  }

  var champ = document.getElementById('champ-recherche');
  var liste = document.getElementById('liste-dossiers');
  if (!champ || !liste) return;
  var cartes = Array.prototype.slice.call(liste.querySelectorAll('.porte'));
  var filtres = Array.prototype.slice.call(document.querySelectorAll('.filtre'));
  var compteur = document.getElementById('nb-resultats');
  var vide = document.getElementById('aucun-resultat');
  var rubrique = 'tous';

  function sansAccents(t) {
    return t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  function appliquer() {
    var mots = sansAccents(champ.value.trim()).split(/\s+/).filter(Boolean);
    var n = 0;
    cartes.forEach(function (c) {
      var texte = sansAccents(c.getAttribute('data-texte') || '');
      var ok = (rubrique === 'tous' || c.getAttribute('data-rubrique') === rubrique) &&
        mots.every(function (m) { return texte.indexOf(m) !== -1; });
      c.hidden = !ok;
      if (ok) n++;
    });
    compteur.textContent = n;
    vide.hidden = n !== 0;
  }
  champ.addEventListener('input', appliquer);
  filtres.forEach(function (f) {
    f.addEventListener('click', function () {
      rubrique = f.getAttribute('data-filtre');
      filtres.forEach(function (g) { g.setAttribute('aria-pressed', String(g === f)); });
      appliquer();
    });
  });
  if (location.hash === '#recherche') champ.focus();
})();
