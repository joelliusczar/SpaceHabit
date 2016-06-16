import MockDatabaseLayer
import AuthenticationLayer
import EverywhereConstants

def insert_one_user():
    cryptPair = AuthenticationLayer.get_new_user_encrypted_details("123456")
    id = MockDatabaseLayer.insert_user("a@b.c",cryptPair[0],cryptPair[1])
    return {EverywhereConstants.ID_KEY:id,MockDatabaseLayer.USER_LOGIN:"a@b.c",
            MockDatabaseLayer.USER_PASSWORD:cryptPair[0],MockDatabaseLayer.USER_SALT:cryptPair[1]}