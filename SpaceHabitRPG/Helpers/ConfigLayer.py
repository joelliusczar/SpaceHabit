import configparser

"""
    this is a wrapper for reading from the config.ini file.
"""

config = configparser.ConfigParser()
config.read('config.ini')

def get_is_debug():
    return config['DEFAULT']['ISDEBUG'] == "true"

def get_access_key():
    key = config['DEFAULT']['AWS_ACCESS_KEY_ID']
    return key


def get_secret_key():
    return config['DEFAULT']['AWS_SECRET_ACCESS_KEY']


def get_region():
    return config['DEFAULT']['REGION']


def get_port():
    if get_is_debug():
        return config['DEBUG']['PORT']
    return config['DEFAULT']['PORT']


def get_url():
    if get_is_debug():
        return config['DEBUG']['URL']
    return config['DEFAULT']['URL']


def get_authentication_server():
    if get_is_debug():
        return config['DEBUG']['AUTHENTICATION_URL']
    return config['DEFAULT']['AUTHENTICATION_URL']

def get_db_name():
    if get_is_debug():
        return config['DEBUG']['DBNAME']
    return config['DEFAULT']['DBNAME']
