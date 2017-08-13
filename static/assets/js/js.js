jQuery(function($) {
	$(document).ready(function() {

		// CACHE

		var html			= $('html'),
			$body			= $('body'),
			wWidth 			= $(window).innerWidth(),
			wHeight 		= $(window).innerHeight(),
			mNav 			= $body.find('.menu-mobile'),
			mNavTrig 		= $body.find('.trigger-menu-mobile'),
			baseUrl			= 'http://' + top.location.host.toString(),
			templateUrl		= baseUrl + '',
			assetsUrl		= templateUrl + '/assets',
			$internalLinks 	= $("a[href^='"+baseUrl+"'], a[href^='/'], a[href^='./'], a[href^='../'], a[href^='#']");


		// COMMON FUNCTIONS

		function baseFx() {

			$.each($internalLinks, function(index, link) {
				$(link).addClass('internal');
			});

			mNavTrig.on('click', function(e) {
				mNav.stop(true, true).slideToggle();
				e.preventDefault();
			})

			$(window).load(function() {

				// remove preload class
				$body.removeClass('preload');

			}); // load
		}


		/* ON DOC READY --------------------------------------*/

		// run base functions 
		baseFx();

		// run page functions
		// if ($body.hasClass('access')) { accessFx(); }



		/* ON WINDOW RESIZE ----------------------------------*/

		$(window).resize(function() {

			wWidth = $(window).innerWidth();
			wHeight = $(window).innerHeight();

		});


		/* ABSTRACTED FUNCTIONS ------------------------------*/

		// activate email links

		function activateEmail (selector) {
			$(selector).html( function() {
				var adr = $(this).data('address');
				var dom = $(this).data('domain');
				var ext = $(this).data('ext');
				return adr + '@' + dom + ext;
			}).attr('href', function() {
				return 'mailto:' + $(this).html();
			}).attr('target', '_blank');
		}

	});

});