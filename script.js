// Proverbs Financial — progressive enhancement

(function () {
  'use strict';

  // Footer year
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Header shadow once the page is scrolled
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Gentle scroll-reveal for key blocks
  var revealSelector = [
    '.hero-inner', '.trust-inner', '.section-head',
    '.chapter', '.pillar', '.step', '.advisor',
    '.philosophy-inner', '.referral-inner',
    '.contact-copy', '.contact-form'
  ].join(',');
  var targets = Array.prototype.slice.call(document.querySelectorAll(revealSelector));

  if ('IntersectionObserver' in window && targets.length) {
    targets.forEach(function (el) { el.classList.add('reveal'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    targets.forEach(function (el) { io.observe(el); });
  }

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
