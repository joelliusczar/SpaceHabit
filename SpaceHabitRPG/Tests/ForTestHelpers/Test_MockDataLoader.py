from SpaceUnitTest import SpaceUnitTest
import MockDatabaseLayer
import MockDataLoader
import EverywhereConstants

class Test_MockDataLoader(SpaceUnitTest):
    def test_insert_one_user(self):
        idStuff = MockDataLoader.insert_one_user()
        self.assertEqual(idStuff[EverywhereConstants.ID_KEY],"users0")
        self.assertEqual(idStuff[MockDatabaseLayer.USER_LOGIN],"a@b.c")
        self.assertEqual(len(idStuff[MockDatabaseLayer.USER_PASSWORD]),87)
        self.assertEqual(len(idStuff[MockDatabaseLayer.USER_SALT]),32)
        stuff = MockDatabaseLayer.get_thing_by_id(idStuff[EverywhereConstants.ID_KEY],MockDatabaseLayer.users)
        self.assertTrue(MockDatabaseLayer.USER_PASSWORD in stuff)
        self.assertTrue(MockDatabaseLayer.USER_LOGIN in stuff)
        self.assertTrue(MockDatabaseLayer.USER_SALT in stuff)
        login = stuff[MockDatabaseLayer.USER_LOGIN]
        self.assertEqual(login,"a@b.c")
        pw = stuff[MockDatabaseLayer.USER_PASSWORD]
        self.assertEqual(len(pw),87)
        salt = stuff[MockDatabaseLayer.USER_SALT]
        self.assertEqual(len(salt),32)


    def test_insert_user_mixed_case(self):
        MockDatabaseLayer.insert_user("A@B.C","123","salt")
        stuff = MockDatabaseLayer.get_user("a@b.c")
        self.assertIsNotNone(stuff)
        self.assertIn(MockDatabaseLayer.USER_DESC, stuff)
        desc = stuff[MockDatabaseLayer.USER_DESC]
        self.assertEqual(desc,"A@B.C")
        login = stuff[MockDatabaseLayer.USER_LOGIN]
        self.assertEqual(login, "a@b.c")

if __name__ == '__main__':
    unittest.main()
