var JobBoardScraper = window.JobBoardScraper || {};

JobBoardScraper = (function ($) {

    'use strict';

    return {

        openLinkInNewWindow: function () {
            $('a.js-external, a[rel="external"]').on('click', function (event) {
                var href;
                href = $(this).attr('href');
                window.open(href);
                event.preventDefault();
            });
        },

        ready: function () {
            this.openLinkInNewWindow();
        }

    };

}(jQuery));

jQuery(document).ready(function () {
    'use strict';
    JobBoardScraper.ready();
});
