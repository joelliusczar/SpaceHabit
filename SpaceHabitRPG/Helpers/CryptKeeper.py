"""
  This module is a wrapper for encryption methods.
"""
from passlib.hash import pbkdf2_sha256


def encrypt_str(str):

  """
    This is a wrapper method for encrypting passwords

    args:
      str: 
        this should be a string. This will be the password you want 
        to encrypt

    returns:
      the pbkdf2_sha256 encrypted version of str, the salt and other 
      useful information is built into it.
      
  """
  hash = pbkdf2_sha256.encrypt(str)
  return hash

def password_is_right(str,hash):
  """
    wrapper to method that checks a password against the saved encrypted 
    password

    args:
      str:
        password sent by the user. We're checking to see if 
        it's the right one
      hash: 
        the encrypted version of the password that was saved in the
        database

    returns:
      true or false: true if the str matches the hash, false if not.

  """
  return pbkdf2_sha256.verify(str,hash)