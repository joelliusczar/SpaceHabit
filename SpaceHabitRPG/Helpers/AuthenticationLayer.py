import CryptKeeper
import UserDBLayer
import Account
import Hero
import re


def is_login_taken(login):
    return UserDBLayer.does_login_exist(login)

def insert_new_user(login,pw,shipName = ""):
    if is_login_taken(login):
        raise FileExistsError("That email is already taken")
    id = safe_insert_new_user(login,pw)
    accountId = Account.create_new_account(id)
    heroId = Hero.create_new_hero(accountId,shipName)
    return (id,accountId,heroId)

def safe_insert_new_user(login,pw):
    cryptPair = get_new_user_encrypted_details(pw)
    safePw = cryptPair[0]
    salt = cryptPair[1]
    id = UserDBLayer.insert_user(login,safePw,salt)
    return id

def get_new_user_encrypted_details(pw):
    salt = CryptKeeper.pass_the_salt()
    safePw = CryptKeeper.encrypt_str(pw,salt)
    return (safePw,salt)

def authenticate_user(login,pw):
    user = UserDBLayer.get_user(login)
    if not user:
        return (False,"#bad_login")
    if not CryptKeeper.password_is_right(pw,user[UserDBLayer.USER_PASSWORD]):
        return (False, "#bad_login_pw")
    return (True,"")

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return "#bad_email"
    if UserDBLayer.does_login_exist(email):
        return "#taken_email"
    return ""

def validate_everything_new_user(email1,email2,pw1,pw2):
    emailErrors = []
    pwErrors = []
    emailValidationResult = validate_email(email1)
    if emailValidationResult:
        emailErrors.append(emailValidationResult)
    if email1 != email2:
        emailErrors.append("#mismatched_email")
    if len(pw1) < 6:
        pwErrors.append("#short_pw")
    if pw1 != pw2:
        pwErrors.append("#mismatched_pw")
    return (emailErrors,pwErrors)