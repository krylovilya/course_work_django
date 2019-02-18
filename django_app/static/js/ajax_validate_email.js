$(document).ready(function () {
    $('#id_email').on("blur", validate);
    function validate() {
        var email = $('#id_email').val();
        $.ajax({
            method: "GET",
            url: "/register/validate_email",
            data: {
                "email": email
            },
            dataType: "json",
            success: function (data) {
                console.log(data);
                if (data.is_taken) {
                    M.toast({html: data.is_taken});
                    $('#reg_btn').attr('disabled', 'disabled');
                }
                else if (data.ok) {
                    $('#reg_btn').removeAttr('disabled');
                }
            },
            error: function () {
                alert("Ошибка ajax запроса");
            }
        })
    }
});
