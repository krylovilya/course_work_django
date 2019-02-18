function like()
{
    var like = $(this);
    var pk = like.data('id');

    $.ajax({
        url : "/like/" + pk,
        type : 'GET',
        data : { 'pk' : pk },

        success : function (json) {
            like.find("[data-count='like']").text(json.like_count);
            if (json.result === "add") {
                M.toast({html: "Лайк поставлен"});
            }
            else if(json.result === "remove") {
                M.toast({html: "Лайк убран"});
            }
            else {
                alert("Ошибка ajax запроса! " + json.result)
            }
            like.text(json.like_count);
        },
        error: function () {
            M.toast({html: "Вы не авторизованы!"});
        }
    });

    return false;
}
$(function() {
    $('[data-count="like"]').click(like);
});
