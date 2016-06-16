"use strict";

$(function () {

    $("#create_account").click(createAccountClick);

    $("#forgot_pw").click(forgotPWClick);

    $("button[name='cancel-add']").click(cancelAddClick);

    $("button[name='pw_cancel']").click(cancelAddClick);

    $("button[name='btnLogin']").click(loginClick);

    $("button[name='save_user']").click(saveUserClick);

    $("#new_user_box").on('hidden.bs.modal', onNewUserModalHide);

    $("input[name='email_input_1']").blur(onEmail1InputBlur);

    $("input[name='email_input_2']").blur(onEmail2InputBlur);

    $("input[name='pw_input_1']").blur(onPw1InputBlur);

    $("input[name='pw_input_2']").blur(onPw2InputBlur);

});

function ValidateInputsMatch(matchClass, caseSensitive) {
    var dotMatchClass = "." + matchClass
    if ($(dotMatchClass).length == 0) {
        throw new RangeError("There are no elements with class " + matchClass);
    }
    var firstValue = $(dotMatchClass).first().val();
    var loopValue = firstValue;
    if (!caseSensitive) {
        firstValue = firstValue.toLowerCase();
    }
    var isMatch = true;
    $(dotMatchClass).each(function () {
        loopValue = $(this).val();
        if (!caseSensitive) {
            loopValue = loopValue.toLowerCase();
        }
        if (firstValue != loopValue) {
            isMatch = false;
            return isMatch;
        }
    });
    return isMatch;
}

function clearNewAccountWindow() {
    $("input[name='email_input_1']").val("");
    $(".validation_message").addClass("hidden");
    $("input[name='email_input_2']").val("");
    $("input[name='pw_input_1']").val("");
    $("input[name='pw_input_2']").val("");
    $("input[name='ship_input']").val("");
}


function createAccountClick() {
    $('#new_user_box').modal('show');
}

function forgotPWClick() {
    $('#forgotten_pw_box').modal('show');
}

function cancelAddClick() {
    $('#new_user_box').modal('hide');
}

function cancelForgotPassword() {
    $('#forgotten_pw_box').modal('hide');
}

function loginClick() {
    $.ajax({
        url: 'login',
        type: 'POST',
        data: {
            'login': $("input[name='input_login']").val(),
            'pw': $("input[name='login_pw']").val()
        },
        success: loginAjaxSuccess
    });
}

function saveUserClick() {
    $.ajax({
        url: 'save_new_user',
        type: 'POST',
        data: {
            'email1': $("input[name='email_input_1']").val(),
            'email2': $("input[name='email_input_1']").val(),
            'pw1': $("input[name='pw_input_1']").val(),
            'pw2': $("input[name='pw_input_2']").val(),
            'shipName': $("input[name='ship_input']").val()
        },
        success: loginAjaxSuccess
    });
}

function onNewUserModalHide() {
    clearNewAccountWindow();
}

function onEmail1InputBlur() {
    $.ajax({
        url: 'validate/email',
        type: 'POST',
        data: { 'email': $("input[name='email_input_1']").val() },
        success: validateNewEmailAjaxSuccess
    });
}

function onEmail2InputBlur() {
    if (ValidateInputsMatch("match_email")) {
        $("#mismatched_email").addClass("hidden");
    }else {
        $("#mismatched_email").removeClass("hidden");
    }
}

function onPw1InputBlur() {
    if ($("input[name='pw_input_1']").val().length < 6) {
        $("#short_pw").removeClass("hidden");
    }
    else {
        $("#short_pw").addClass("hidden");
    }
}

function onPw2InputBlur() {

    if (ValidateInputsMatch("match_pw",true)) {
        $("#mismatched_pw").addClass("hidden");
    }
    else {
        $("#mismatched_pw").removeClass("hidden");
    }
}

function validateNewEmailAjaxSuccess(data) {
    if (data) {
        $('.validation_success').addClass("hidden");
        $(data).removeClass("hidden");
    }
    else {
        $('.validation_success').removeClass("hidden");
        $('.email_error').addClass("hidden");
    }
}

function loginAjaxSuccess(data) {

    $(".login_error").addClass("hidden");

    if (data['success']) {
        window.location.replace("/")
    }
    else {
        var errors = data['errors'];
        for(var i = 0; i < errors.length; i++){
            $(errors[i]).removeClass("hidden");
        }
    }
}

