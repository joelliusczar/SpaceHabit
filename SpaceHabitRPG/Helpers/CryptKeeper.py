import uuid
from passlib.hash import pbkdf2_sha256


def pass_the_salt():
    return uuid.uuid4().hex

def encrypt_str(str,salt = None):
    hash = pbkdf2_sha256.encrypt(str)
    return hash

def password_is_right(str,hash,salt = None):
    return pbkdf2_sha256.verify(str,hash)