(function(){

	'use strict'


	var siteMenuToggle = function() {
		// Click js-menu-toggle

		var menuToggle = document.querySelectorAll(".js-menu-toggle");
		var siteMobileMenu = document.querySelector(".site-mobile-menu");

		var setMenuOpen = function(isOpen) {
			document.body.classList.toggle('offcanvas-menu', isOpen);
			siteMobileMenu.setAttribute('aria-hidden', String(!isOpen));
			menuToggle.forEach(toggle => {
				toggle.classList.toggle('active', isOpen);
				toggle.setAttribute('aria-expanded', String(isOpen));
				toggle.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
			});
		};

		menuToggle.forEach(toggle => {
			toggle.addEventListener("click", () => {
				setMenuOpen(!document.body.classList.contains('offcanvas-menu'));
			});
		});

		document.addEventListener('click', function(event) {
			var isClickInside = siteMobileMenu.contains(event.target);
			var isToggle = Array.prototype.some.call(menuToggle, toggle => {
				return toggle.contains(event.target);
			});

			if (!isClickInside && !isToggle && document.body.classList.contains('offcanvas-menu')) {
				setMenuOpen(false);
			}

		});

	}; 
	siteMenuToggle();


})()