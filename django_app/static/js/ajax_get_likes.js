$(document).ready(function () {
    function get_likes() {
        var pin_id = $('#pin_id').val();
        $.ajax({
            method: "GET",
            url: "/get_likes_from_id",
            data: {
                "pin_id": pin_id
            },
            dataType: "json",
            success: function (data) {
                console.log(data);
                if (data.is_taken) {
                    $('#'+ pin_id).text(data.like);
                }
            },
            error: function () {
                alert("Ошибка ajax запроса");
            }
        })
    }
});