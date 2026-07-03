// Proverbs Financial — progressive enhancement

(function () {
  'use strict';

  // Footer year
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Contact form — client-side validation + friendly confirmation.
  // No backend is wired up yet. To collect real submissions, POST to your
  // endpoint or a form service (Formspree, Netlify Forms) in the success block.
  var form = document.getElementById('contact-form');
  var note = document.getElementById('form-note');
  if (form && note) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      note.className = 'form-note';
      note.textContent = '';

      var name = form.name.value.trim();
      var email = form.email.value.trim();
      var emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

      if (!name) {
        note.classList.add('err');
        note.textContent = 'Please tell us your name.';
        form.name.focus();
        return;
      }
      if (!emailOk) {
        note.classList.add('err');
        note.textContent = 'Please enter a valid email address.';
        form.email.focus();
        return;
      }

      note.classList.add('ok');
      note.textContent =
        'Thank you, ' + name.split(' ')[0] + '. Your note is on its way — we’ll be in touch personally.';
      form.reset();
    });
  }
})();
