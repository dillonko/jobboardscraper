var TimGorin = window.TimGorin || {};

TimGorin = (function ($) {

    'use strict';

    return {

        openLinkInNewWindow: function () {
            $('a.external, a[rel="external"]').on('click', function (event) {
                var href;
                href = $(this).attr('href');
                window.open(href);
                event.preventDefault();
            });
        },

        init: function () {
            this.openLinkInNewWindow();
        }
    };

}(window.jQuery));

jQuery(function () {
    'use strict';
    TimGorin.init();
});
