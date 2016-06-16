import CryptKeeper
import UserDBLayer
import Account
import Hero
import re
import cherrypy
import EverywhereConstants as consts

"""
    This module contains all that methods that determine if user provided details
    are correct. 

"""


def is_login_taken(login):
    return UserDBLayer.does_login_exist(login)


def insert_new_user(login,pw,shipName = ""):
    """
        This used during the create new user process
        saves a new user to the database
        
        args:
            login: 
                unique email address supplied by the user
            pw: 
                password supplied by the user. 
            shipName: 
                The space ship name is supplied by the user. 
                Not required but lame if not there.
        returns:
            a tuple containing the primary key of the newly inserted user from the
            User table, the primary key of the account created for the new user,
            and the primary key of the hero created for the new user.
    """
    if is_login_taken(login):
        raise FileExistsError("That email is already taken")
    id = safe_insert_new_user(login,pw)
    accountId = Account.create_new_account(id)
    heroId = Hero.create_new_hero(accountId,shipName)
    return (id,accountId,heroId)


def get_existing_user_details(login):
    """
    """
    userid = UserDBLayer.get_user(login)
    #accountId = Account.Account(


def safe_insert_new_user(login,pw):
    """
        This used during the create new user process.
        this should be called when doing the actual inserting of a new user.
        This encrypts the password before saving.

        args:
            login: 
                unique email address supplied by the user
            pw: 
                the unencrypted password supplied by the user.

        returns:
            the primary key returned from the Database upon insertion of 
            the new user
    """
    safePw = CryptKeeper.encrypt_str(pw)
    id = UserDBLayer.insert_user(login,safePw)
    return id


def authenticate_user(login,pw):
    """
        This is used during the login process.
        Determines if the user is trying to log on with a valid login and
        also determines if the user is trying to log on with a correct password

        args:
            login: 
                email address supplied by the user
            pw: 
                the unencrypted password supplied by the user.

        returns:
            a dict with two keys, a boolean: 'success' and list: 'errors.'
            'success' tells the caller whether or not the login attempt was successful.
            If it was 'success' is true, then 'errors' should be an empty list.
            If 'success' is false, then 'errors' will have between one 
            and two elements. Each of them will be id-css selectors for jquery
            to use.
    """
    user = UserDBLayer.get_user(login)
    resultDict = {'messages':[],'success':False}
    if not user:
        resultDict['messages'].append("#bad_login")
        return resultDict
    if not CryptKeeper.password_is_right(pw,user[UserDBLayer.USER_PASSWORD]):
        resultDict['messages'].append("#bad_login_pw")
        return resultDict
    resultDict['success'] = True
    return resultDict


def validate_email(email):
    """
        This used during the create new user process.
        determines if the email supplied is formatted correctly and doesn't
        already exist.

        args:
            email:
                An email address supplied by the user

        returns:
            a dict with two keys, a boolean: 'success' and list: 'errors.'
            'success' tells the caller whether or not the login attempt was successful.
            If it was 'success' is true, then 'errors' should be an empty list.
            If 'success' is false, then 'errors' will have between one 
            and two elements. Each of them will be id-css selectors for jquery
            to use.
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return {'success': False,'messages':["#bad_email"]}
    if UserDBLayer.does_login_exist(email):
        return {'success': False,'messages':["#taken_email"]}
    return {'success': True,'messages':["#good_email"]}


def check_all_new_user_validations(email1,email2,pw1,pw2,shipName):
    """
        This used during the create new user process.
        This method calls other validation methods and baically determines
        if any of the info that the user entered was illegal.

        args:
            all args should be strings and less than 256 characters else
            this will return invalid.

            email1: 
                this should be input that will also pass the 
                validate_email test
            email2: 
                this should match email1.
            pw1: 
                this only needs to pass any password complexity requirements
                that have been added to the method. Currently the only 
                requirement is that the password must be at least 6
                characters.
            pw2: 
                this should match pw1:

        returns:
            a list of violations that either the user's email or password 
            commits. An empty list implies that everything is dandy.

    """
    flags = []
    if len(email1) <= 256:
        emailValidationResult = validate_email(email1)
        if not emailValidationResult['success']:
            flags.extend( emailValidationResult['errors'])
        if email1 != email2:
            flags.append( "#mismatched_email")
    else:
        if len(email1) > 256:
            flags.append("#email1_too_long")
        if len(email2) > 256:
            flags.append("#email2_too_long")
    if len(pw1) <= 256:
        if len(pw1) < 6:
            flags.append("#short_pw")
        if pw1 != pw2:
            flags.append("#mismatched_pw")
    else:
        if len(pw1) > 256:
            flags.append("pw1_too_long")
        if len(pw2) > 256:
            flags.append("pw2_too_long")
    if len(shipName) > 256:
        flags.append("#shipname_too_long")
    return flags

#disableAuthenticationRedirects should only ever be used in testing. 
#Never in production
disableAuthenticationRedirects = False

def redirect_unauthenticated():
    """
        a cherrypy decororator. Place the decorator infront of controller
        methods that return parts of the website which the user needs to be
        logged in to see. If they are not logged in, redirect them to the 
        login page.
    """
    if disableAuthenticationRedirects:
        return
    username = cherrypy.session.get(consts.SESSION_KEY)
    if not username:
        raise cherrypy.HTTPRedirect("/login")

def redirect_authenticated():
    """
        a cherrypy decororator. Place the decorator infront of controller
        methods that return the login part of the website.
        If they are already logged in, redirect them to the main page.
    """
    if disableAuthenticationRedirects:
        return
    username = cherrypy.session.get(consts.SESSION_KEY)
    if username:
        raise cherrypy.HTTPRedirect("/")

#These are useable as soon as I import AuthenticationLayer
cherrypy.tools.redirect_unauthenticated = cherrypy.Tool("before_handler",redirect_unauthenticated)
cherrypy.tools.redirect_authenticated = cherrypy.Tool("before_handler",redirect_authenticated)
