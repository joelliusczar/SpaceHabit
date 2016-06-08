import unittest
import MockDataLoader
import MockDatabaseLayer

class Test_MockDataLoaderTests(unittest.TestCase):

    def test_insert_one_user(self):
        id = MockDataLoader.insert_one_user()
        self.assertEqual(id,"users0")
        stuff = MockDatabaseLayer.get_thing_by_id(id,MockDatabaseLayer.users)
        self.assertTrue(MockDatabaseLayer.USER_PASSWORD in stuff)
        self.assertTrue(MockDatabaseLayer.USER_LOGIN in stuff)
        self.assertTrue(MockDatabaseLayer.USER_SALT in stuff)
        login = stuff[MockDatabaseLayer.USER_LOGIN]
        self.assertEqual(login,"a@b.c")
        pw = stuff[MockDatabaseLayer.USER_PASSWORD]
        self.assertEqual(len(pw),87)
        salt = stuff[MockDatabaseLayer.USER_SALT]
        self.assertEqual(len(salt),32)

if __name__ == '__main__':
    unittest.main()
