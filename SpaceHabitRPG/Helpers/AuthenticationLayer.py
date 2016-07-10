"""
  This module contains all that methods that determine if user provided details
  are correct. 

"""
from AllDBFields import BaseFields
from AllDBFields import AuthenticationFields
import CryptKeeper
import DatabaseLayer
import re
import cherrypy





def is_login_taken(login):
  """
    checks the database to determine if an email address has already been used.

    args:
      login: 
        this should be an email address
    returns:
      a boolean. true if email is already used. false if not.
  """
  collection = DatabaseLayer.get_table(AuthenticationFields.COLLECTION_NAME)
  if collection.find({AuthenticationFields.USER_LOGIN:login.lower()})\
      .count() > 0:
    return True
  else:
    return False


def get_user(login):
  """
    gets the user data from the database

    args:
      this should be an email address
    returns:
      a dict containing, the user email address in forced lower case,
      the users encrypted password, and the user's email address in whatever
      case they saved it as.
  """
  collection = DatabaseLayer.get_table(AuthenticationFields.COLLECTION_NAME)
  return collection.find_one({AuthenticationFields.USER_LOGIN:login.lower()})


def insert_new_user(login,pw,shipName=""):
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
  from Account import Account
  from Hero import Hero

  if is_login_taken(login):
    raise FileExistsError("That email is already taken")
  loginPk = safe_insert_new_user(login,pw)
  accountId = Account.create_new_account_in_db(loginPk)
  heroId = Hero.construct_new_hero_in_db(accountId,shipName)
  return (loginPk,accountId,heroId)


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
  collection = DatabaseLayer.get_table(AuthenticationFields.COLLECTION_NAME)
  id = collection.insert_one({AuthenticationFields.USER_LOGIN:login.lower(),
    AuthenticationFields.USER_PASSWORD:safePw,
    AuthenticationFields.USER_DESC: login}).inserted_id
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
  user = get_user(login)
  resultDict = {'messages':[],'success':False}
  if not user:
    resultDict['messages'].append("#bad_login")
    return resultDict
  if not CryptKeeper.password_is_right(\
        pw,user[AuthenticationFields.USER_PASSWORD]):
    resultDict['messages'].append("#bad_login_pw")
    return resultDict
  resultDict['success'] = True
  return resultDict

def get_loginPk_by_login(validLogin):
  """
    args:
      validLogin:
        I'm gonna assume that this login has already been vetted earlier
        in the program.
      return:
        an objectId to the users collection
  """
  collection = DatabaseLayer.get_table(AuthenticationFields.COLLECTION_NAME)
  login = collection.find_one({AuthenticationFields.USER_LOGIN: validLogin})
  return login[BaseFields.PK_KEY]
  

def get_accountPk_by_loginPk(loginPk):
  """
    args:
      loginPk:
        an fk to the user collection
      return:
        an objectId to the account collection
  """
  from AllDBFields import AccountFields
  collection = DatabaseLayer.get_table(AccountFields.COLLECTION_NAME)
  account = collection.find_one({AccountFields.LOGIN_PK_KEY:loginPk})
  return account[AccountFields.PK_KEY]

def get_heroPk_by_accountPk(accountPk):
  """
    args:
      userId:
        an fk to the account collection
      return:
        an objectId to the hero collection
  """
  from AllDBFields import HeroDbFields
  collection = DatabaseLayer.get_table(HeroDbFields.COLLECTION_NAME)
  hero = collection.find_one({HeroDbFields.ACCOUNT_PK_KEY:accountPk})
  return hero[HeroDbFields.PK_KEY]



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
  if is_login_taken(email):
    return {'success': False,'messages':["#taken_email"]}
  return {'success': True,'messages':["#good_email"]}



def check_all_validations_for_new_login(email1,email2,pw1,pw2,shipName):
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
      flags.extend(emailValidationResult['messages'])
    if email1 != email2:
      flags.append("#mismatched_email")
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
  username = cherrypy.session.get(BaseFields.SESSION_KEY)
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
  username = cherrypy.session.get(BaseFields.SESSION_KEY)
  if username:
    raise cherrypy.HTTPRedirect("/")

#These are useable as soon as I import AuthenticationLayer
cherrypy.tools.redirect_unauthenticated = cherrypy.Tool("before_handler",redirect_unauthenticated)
cherrypy.tools.redirect_authenticated = cherrypy.Tool("before_handler",redirect_authenticated)
