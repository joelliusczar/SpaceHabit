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
        result = auth.insert_new_user("a@b.c","p","s")
        self.assertEqual(result[0],MockDatabaseLayer.users+"0")
        self.assertEqual(result[1],MockDatabaseLayer.accounts+"1")
        self.assertEqual(result[2],MockDatabaseLayer.heros+"2")

    def test_is_login_taken(self):
        t = auth.is_login_taken("a@b.c")
        self.assertFalse(t)
        auth.insert_new_user("b@c.d","p","s")
        t = auth.is_login_taken("b@c.d")
        self.assertTrue(t)

    def test_authenticate_user(self):
        auth.insert_new_user("c@d.e","p","s")
        result = auth.authenticate_user("d@e.f","")
        self.assertEqual(result[1],"#bad_login")
        result = auth.authenticate_user("c@d.e","123")
        self.assertEqual(result[1],"#bad_login_pw")
        result = auth.authenticate_user("c@d.e","p")
        self.assertEqual(result[1],"")
        self.assertTrue(result[0])

    def test_validate_email(self):
        auth.insert_new_user("a@b.c","p","s")
        t = auth.validate_email("@@")
        self.assertEqual(t,"#bad_email")
        t = auth.validate_email("a@b.c")
        self.assertEqual(t,"#taken_email")
        t = auth.validate_email("b@c.d")
        self.assertEqual(t,"")

    def test_validate_everything_new_user_bad_email(self):
        t = auth.validate_everything_new_user("bademail","bademail","123456","123456")
        self.assertEqual(len(t[0]),1)
        self.assertEqual(len(t[1]),0)
        self.assertEqual(t[0][0],"#bad_email")
        

    def test_validate_everything_new_user_bad_mismatched_email(self):
        t = auth.validate_everything_new_user("bademail","verybademail","123456","123456")
        self.assertEqual(len(t[0]),2)
        self.assertEqual(len(t[1]),0)
        self.assertEqual(t[0][0],"#bad_email")
        self.assertEqual(t[0][1],"#mismatched_email")

    def test_validate_everything_new_user_bad_pw(self):
        t = auth.validate_everything_new_user("bademail","verybademail","123","123")
        self.assertEqual(len(t[0]),2)
        self.assertEqual(len(t[1]),1)
        self.assertEqual(t[0][0],"#bad_email")
        self.assertEqual(t[0][1],"#mismatched_email")
        self.assertEqual(t[1][0],"#short_pw")

    def test_validate_everything_new_user_bad_mismatched_pw(self):
        t = auth.validate_everything_new_user("bademail","verybademail","123","abc")
        self.assertEqual(len(t[0]),2)
        self.assertEqual(len(t[1]),2)
        self.assertEqual(t[0][0],"#bad_email")
        self.assertEqual(t[0][1],"#mismatched_email")
        self.assertEqual(t[1][0],"#short_pw")
        self.assertEqual(t[1][1],"#mismatched_pw")

    def test_validate_everything_good_user_pw(self):
        t = auth.validate_everything_new_user("a@b.c","a@b.c","123456","123456")
        self.assertEqual(len(t[0]),0)
        self.assertEqual(len(t[1]),0)


if __name__ == '__main__':
    unittest.main()
