window.get_pin = function(pin_id) {
    $.ajax({
        method: "GET",
        url: "/get_pin/",
        cache: false,
        data: {
            "pin_id": pin_id
        },
        dataType: "json",
        success: function (data) {
            console.log(data);
            //$('.gallery').prepend(data.html);
            //$masonry.append( data.html ).masonry( 'appended', data.html);
            //$masonry.append(data.html).masonry('appended', data.html);
            //$masonry.masonry('layout');
            //$masonry.imagesLoaded(function() {
            //    $masonry.masonry('layout');
            //});
            //$('.gallery-expand').galleryExpand('open');
            /*$masonry = $('.gallery');
            $masonry.masonry({
                // set itemSelector so .grid-sizer is not used in layout
                itemSelector: '.gallery-item',
                // use element for option
                columnWidth: '.gallery-item',
                // no transitions
                transitionDuration: '0.4s',
                singleMode: true,
                isResizable: true,
            }); */
            var jdata = jQuery(data.html);
            window.$masonry.append(jdata);
            window.$masonry.masonry('appended', jdata);
            //$masonry.masonry( 'layout' );
            window.$masonry.imagesLoaded();
            $('a.filter').click(function (e) {
                e.preventDefault();
            });

            window.$masonry.masonry( 'reloadItems' );

        },
        error: function () {
            alert("Ошибка ajax запроса");
        }
    })
};
//get_pin(0 );
