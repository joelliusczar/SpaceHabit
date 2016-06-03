import unittest
import DatabaseLayer
import UserDBLayer
import MockDatabaseLayer
import AuthenticationLayer as auth

class Test_AuthenticationLayerTests(unittest.TestCase):

    def setUp(self):
        import MockSetUp
        MockSetUp.set_up_mock_db_connections()
        return super().setUp()

    def tearDown(self):
        MockDatabaseLayer.clean_up()
        return super().tearDown()

    def test_insert_new_user(self):
        result = auth.insert_new_user("a","p","s")
        self.assertEqual(result[0],MockDatabaseLayer.users+"0")
        self.assertEqual(result[1],MockDatabaseLayer.accounts+"1")
        self.assertEqual(result[2],MockDatabaseLayer.heros+"2")

    def test_is_login_taken(self):
        t = auth.is_login_taken("a")
        self.assertFalse(t)
        auth.insert_new_user("b","p","s")
        t = auth.is_login_taken("b")
        self.assertTrue(t)

    def test_authenticate_user(self):
        auth.insert_new_user("c","p","s")
        result = auth.authenticate_user("d","")
        self.assertEqual(result[1],"#bad_login")
        result = auth.authenticate_user("c","123")
        self.assertEqual(result[1],"#bad_login_pw")
        result = auth.authenticate_user("c","p")
        self.assertEqual(result[1],"")
        self.assertTrue(result[0])

    def test_validate_email(self):
        auth.insert_new_user("a","p","s")
        t = auth.validate_email("@@")
        self.assertEqual(t,"#bad_email")
        t = auth.validate_email("a")
        self.assertEqual(t,"#taken_email")
        t = auth.validate_email("b")
        self.assertEqual(t,"")


if __name__ == '__main__':
    unittest.main()
