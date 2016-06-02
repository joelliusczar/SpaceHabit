$(function () {

    $("#create_account").click(function () {
        $('#new_user_box').modal('show');
    });

    $("#forgot_pw").click(function () {
        $('#forgotten_pw_box').modal('show');
    });

    $("button[name='cancel']").click(function () {
        $('#new_user_box').modal('hide');
    });

    $("button[name='btnLogin']").click(function () {
        console.log("click click motherfucker")
        $.ajax({
            url: 'login',
            type: 'POST',
            data: {
                'login': $("input[name='input_login']").val(),
                'pw': $("input[name='input_pw']").val()
            },
            success: function (data) {
                if (data) {
                    console.log(data);
                }
                else {
                    window.location.replace("/")
                }
            }
        });
    });

    $("button[name='save_user']").click(function () {
        $.ajax({
            url: 'save_new_user',
            type: 'POST',
            data: {'email1':$("input[name='email_input_1']").val(),
                'email2':$("input[name='email_input_1']").val(),
                'pw1':$("input[name='pw_input_1']").val(),
                'pw2': $("input[name='pw_input_2']").val(),
                'shipname': $("input[name='ship_input']").val()
            },
            success: function(data) {
                if (data) {
                    console.log(data);
                }
                else {
                    window.location.replace("/")
                }
            }
        });
    });

    $("#new_user_box").on('hidden.bs.modal', function (e) {
        
    });

    $("input[name='email_input_1']").blur(function () {
        $.ajax({
            url: 'validate/email',
            type: 'POST',
            data: { 'email': $("input[name='email_input_1']").val() },
            success: function (data) {
                if (data) {
                    $('.validation_success').addClass("hidden");
                    $(data).removeClass("hidden");
                }
                else {
                    $('.validation_success').removeClass("hidden");
                    $('.email_error').addClass("hidden");
                }
            }
        });
    });

    $("input[name='email_input_2']").blur(function () {
        if ($("input[name='email_input_1']").val() != $("input[name='email_input_2']").val()) {
            $("#mismatched_email").removeClass("hidden");
        }
        else {
            $("#mismatched_email").addClass("hidden");
        }
    });

    $("input[name='pw_input_1']").blur(function () {
        if ($("input[name='pw_input_1']").val().length < 6) {
            $("#short_pw").removeClass("hidden");
        }
        else {
            $("#short_pw").addClass("hidden");
        }
    });

    $("input[name='pw_input_2']").blur(function () {
        if ($("input[name='pw_input_1']").val() != $("input[name='pw_input_2']").val()) {
            $("#mismatched_pw").removeClass("hidden");
        }
        else {
            $("#mismatched_pw").addClass("hidden");
        }
    });

    


});


function clearNewAccountWindow() {
    $("input[name='email_input_1']").val("");
    $("#email_validation").html("");
    $("input[name='email_input_2']").val("");
    $("input[name='pw_input_1']").val("");
    $("#pw_validation").html("");
    $("input[name='pw_input_2']").val("");
}

