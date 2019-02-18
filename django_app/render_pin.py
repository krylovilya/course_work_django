def render_pin(pin):
    html = (
            '<div class="col l4 m6 s12 gallery-item gallery-expand sintel" style="float: left;">' +
            '<div class="gallery-curve-wrapper">' +
            '<a class="gallery-cover gray filter">' +
            '<img src="{0}" alt="placeholder" style="width: 100%; border: none;">' +
            '</a>' +
            '<div class="gallery-header">' +
            '<span>{1}</span>' +
            '</div>' +
            '<div class="gallery-body">' +
            '<div class="title-wrapper">' +
            '<h3> {1} </h3>' +
            '<h5>Автор {2}</h5>' +
            '<p><span>Лайков: {3}</span></p>' +
            '</div>' +
            '<p class="description">' +
            '{4}' +
            '</p>' +
            '</div>' +
            '<div class="gallery-action">' +
            '<a class="btn-floating btn-large waves-effect' +
            'waves-light"><i class="material-icons">favorite</i></a>' +
            '</div>' +
            '</div>' +
            '</div>').format(pin.photo, pin.title, pin.autor.username, pin.likes, pin.text, html="")
    # 'photo': pin.photo,
    # 'title': pin.title,
    # 'autor_username': pin.autor.username,
    # 'likes': pin.likes,
    # 'text': pin.text
    # })
    return html
