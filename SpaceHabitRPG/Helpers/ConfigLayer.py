import configparser

config = configparser.ConfigParser()
config.read('config.ini')
def get_access_key():
    key = config['DEFAULT']['AWS_ACCESS_KEY_ID']
    return key
def get_secret_key():
    return config['DEFAULT']['AWS_SECRET_ACCESS_KEY']
def get_region():
    return config['DEFAULT']['REGION']
def get_port():
    if config['DEFAULT']['ISDEBUG'] == "true":
        return config['DEBUG']['PORT']
    return config['DEFAULT']['PORT']
def get_url():
    if config['DEFAULT']['ISDEBUG'] == "true":
        return config['DEBUG']['URL']
    return config['DEFAULT']['URL']

def get_db_name():
    if config['DEFAULT']['ISDEBUG'] == "true":
        return config['DEBUG']['DBNAME']
    return config['DEFAULT']['DBNAME']
