/* KALO Gifts theme scripts. No dependencies. */
(function () {
  'use strict';

  /* mobile menu */
  var toggle = document.querySelector('[data-menu-toggle]');
  var nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
  }

  /* countdown */
  var cd = document.querySelector('[data-countdown]');
  if (cd) {
    var target = new Date(cd.getAttribute('data-countdown'));
    var note = document.querySelector('[data-cd-note]');
    var pad = function (n) { return String(n).padStart(2, '0'); };
    var tick = function () {
      var d = Math.max(0, target - new Date());
      cd.querySelector('[data-d]').textContent = Math.floor(d / 864e5);
      cd.querySelector('[data-h]').textContent = pad(Math.floor(d % 864e5 / 36e5));
      cd.querySelector('[data-m]').textContent = pad(Math.floor(d % 36e5 / 6e4));
      cd.querySelector('[data-s]').textContent = pad(Math.floor(d % 6e4 / 1e3));
      if (d === 0 && note) note.textContent = 'Merry Christmas. Thank you for celebrating with us.';
    };
    tick();
    setInterval(tick, 1000);
  }

  /* product form: variant selection, price, quantity, gallery */
  var form = document.querySelector('[data-product-form]');
  if (form) {
    var json = document.querySelector('[data-product-json]');
    var product = json ? JSON.parse(json.textContent) : null;
    var idInput = form.querySelector('[name=id]');
    var priceEl = document.querySelector('[data-price]');
    var btn = form.querySelector('[data-add]');
    var fmt = new Intl.NumberFormat('en-IN', { style: 'currency', currency: (window.Shopify && Shopify.currency && Shopify.currency.active) || 'INR', maximumFractionDigits: 0 });

    var update = function () {
      if (!product) return;
      var chosen = [];
      form.querySelectorAll('.opt').forEach(function (g) {
        var c = g.querySelector('input:checked');
        chosen.push(c ? c.value : null);
      });
      var v = product.variants.find(function (x) {
        return x.options.every(function (o, i) { return chosen[i] === null || chosen[i] === o; });
      });
      if (!v) { if (btn) { btn.disabled = true; btn.querySelector('span').textContent = 'Unavailable'; } return; }
      idInput.value = v.id;
      if (priceEl) priceEl.textContent = fmt.format(v.price / 100);
      if (btn) {
        btn.disabled = !v.available;
        btn.querySelector('span').textContent = v.available ? 'Add to bag' : 'Sold out';
      }
      var wa = document.querySelector('[data-wa]');
      if (wa) {
        var msg = "Hi KALO! I'd like to customise: " + wa.getAttribute('data-wa-title') +
          (product.variants.length > 1 ? ' (' + v.options.join(', ') + ')' : '') + ' ' + wa.getAttribute('data-wa-url');
        wa.href = 'https://wa.me/' + wa.getAttribute('data-wa') + '?text=' + encodeURIComponent(msg);
      }
      var url = new URL(location.href);
      url.searchParams.set('variant', v.id);
      history.replaceState({}, '', url);
    };
    form.addEventListener('change', update);
    update();

    var q = form.querySelector('[data-qty]');
    form.querySelectorAll('[data-step]').forEach(function (b) {
      b.addEventListener('click', function () {
        var n = Math.max(1, (parseInt(q.value, 10) || 1) + parseInt(b.getAttribute('data-step'), 10));
        q.value = n;
      });
    });

  }

  document.querySelectorAll('[data-thumb]').forEach(function (b) {
    b.addEventListener('click', function () {
      var main = document.querySelector('.pdp .gallery .frame img');
      if (main) { main.src = b.getAttribute('data-src'); main.removeAttribute('srcset'); }
    });
  });
})();
