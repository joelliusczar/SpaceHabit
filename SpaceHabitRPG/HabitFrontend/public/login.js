"use strict";

$(function () {

    $("#create_account").click(createAccountClick);

    $("#forgot_pw").click(forgotPWClick);

    $("button[name='cancel-add']").click(cancelAddClick);

    $("button[name='send_recovery']").click(cancelAddClick);

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
    /*
        checks any elements with a given class and checks to ensure that their
        text match.

        args:
            matchClass:
                this should be a string, specifically, the name of a class
                withot the dot.
            caseSensitive:
                true -> abc != ABC
                false -> abc == ABC
        returns:
            either true or false. if the values for all of the selected 
            elements match then return true, otherwise return false.
    */
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
    /*
        makes error messages invisible and clears away all input text
        in the new account modal.
    */
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

function sendPasswordToEmailClick() {
    /*
        #TODO
    */
    alert("this is not finished.");
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
    /*
        if the emails match, hide any previous error messages about mismatched
        emails, but if they don't match, show the errors.
    */

    if (ValidateInputsMatch("match_email")) {
        $("#mismatched_email").addClass("hidden");
    }else {
        $("#mismatched_email").removeClass("hidden");
    }
}


function onPw1InputBlur() {
    /*
        checks that the password entered by the user is a minimum length
    */
    if ($("input[name='pw_input_1']").val().length < 6) {
        $("#short_pw").removeClass("hidden");
    }
    else {
        $("#short_pw").addClass("hidden");
    }
}


function onPw2InputBlur() {
    /*
        if the passwords match, hide any previous error messages about mismatched
        passwords, but if they don't match, show the errors.
    */

    if (ValidateInputsMatch("match_pw",true)) {
        $("#mismatched_pw").addClass("hidden");
    }
    else {
        $("#mismatched_pw").removeClass("hidden");
    }
}


function validateNewEmailAjaxSuccess(data) {
    /*
        this is called in response to a server call.
        If our email was invalid, show error messages.
        If email was valid, show success message.
        hides any previous error messages.

        args:
            data: 
                expected to be a js dict with two memebers. The first is
                messages which is an array of jquery,css id selectors, i.e. 
                strings. The second memeber is success which is a boolean 
                which tells us if the email was acceptable. True: acceptable
                false: not acceptable
    */
    $(".validation_message").addClass("hidden")
    var messages = data.messages;
    for (var i = 0; i < messages.length; i++) {
        $(messages[i]).removeClass("hidden");
    }
}


function loginAjaxSuccess(data) {
    /*
        this method is used to redirect the page from the login page upon
        successful login.
        this is also called upon successful user creation.

        args:
            data:
                expected to be a js dict with two memebers. The first is
                messages which is an array of jquery,css id selectors, i.e. 
                strings. The second memeber is success which is a boolean 
                which tells us if the login attempt was acceptable. True: acceptable
                false: not acceptable
    */
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

function ajaxError() {
    /*
        simple method to let the user know if the server is not
        responding for some reason.
    */
    alert("There was an error with this request. Please try again later.");
}

