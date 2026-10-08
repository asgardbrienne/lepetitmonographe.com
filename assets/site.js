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

  var haut = document.querySelector('.haut-de-page');
  if (haut) {
    var maj = function () { haut.classList.toggle('visible', window.scrollY > 900); };
    window.addEventListener('scroll', maj, { passive: true });
    maj();
  }

  // Sommaire : fermé par défaut sur petit écran
  var sommaire = document.querySelector('.sommaire');
  if (sommaire && window.matchMedia('(max-width: 999px)').matches) sommaire.removeAttribute('open');

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
