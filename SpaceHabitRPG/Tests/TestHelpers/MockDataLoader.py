import MockDatabaseLayer
import AuthenticationLayer

def insert_one_user():
    cryptPair = AuthenticationLayer.get_new_user_encrypted_details("123456")
    id = MockDatabaseLayer.insert_user("a@b.c",cryptPair[0],cryptPair[1])
    return id