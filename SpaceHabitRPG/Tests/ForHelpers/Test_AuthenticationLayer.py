from SpaceUnitTest import SpaceUnitTest
import DatabaseLayer
import UserDBLayer
import MockDatabaseLayer
import AuthenticationLayer as auth

class Test_AuthenticationLayerTests(SpaceUnitTest):

    @classmethod
    def setUpClass(cls):
        import MockSetUp
        MockSetUp.set_up_mock_db_connections()
        return super().setUpClass()

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
        self.assertEqual(len(result['errors']),1)
        self.assertEqual(result['errors'][0],"#bad_login")
        result = auth.authenticate_user("c@d.e","123")
        self.assertEqual(len(result['errors']),1)
        self.assertEqual(result['errors'][0],"#bad_login_pw")
        result = auth.authenticate_user("c@d.e","p")
        self.assertEqual(len(result['errors']),0)
        self.assertTrue(result['success'])

    def test_validate_email(self):
        auth.insert_new_user("a@b.c","p","s")
        t = auth.validate_email("@@")
        self.assertFalse(t['success'])
        self.assertEqual(t['messages'][0],"#bad_email")
        t = auth.validate_email("a@b.c")
        self.assertFalse(t['success'])
        self.assertEqual(t['messages'][0],"#taken_email")
        t = auth.validate_email("b@c.d")
        self.assertTrue(t['success'])
        self.assertEqual(t['messages'][0],"#good_email")

    def test_validate_everything_new_user_bad_email(self):
        t = auth.check_all_new_user_validations("bademail","bademail","123456","123456","ship")
        self.assertEqual(len(t),1)
        self.assertEqual(t[0],"#bad_email")
        

    def test_validate_everything_new_user_bad_mismatched_email(self):
        t = auth.check_all_new_user_validations("bademail","verybademail","123456","123456","ship")
        self.assertEqual(len(t),2)
        self.assertIn("#bad_email",t)
        self.assertIn("#mismatched_email",t)

    def test_validate_everything_new_user_bad_pw(self):
        t = auth.check_all_new_user_validations("bademail","verybademail","123","123","ship")
        self.assertEqual(len(t),3)
        self.assertIn("#bad_email",t)
        self.assertIn("#mismatched_email",t)
        self.assertIn("#short_pw",t)


    def test_validate_everything_new_user_bad_mismatched_pw(self):
        t = auth.check_all_new_user_validations("bademail","verybademail","123","abc","ship")
        self.assertEqual(len(t),4)
        self.assertIn("#bad_email",t)
        self.assertIn("#mismatched_email",t)
        self.assertIn("#short_pw",t)
        self.assertIn("#mismatched_pw",t)


    def test_validate_everything_good_user_pw(self):
        t = auth.check_all_new_user_validations("a@b.c","a@b.c","123456","123456","ship")
        self.assertEqual(len(t),0)


    def test_safe_insert_new_user(self):
        id = auth.safe_insert_new_user("a","123")
        self.assertEqual(id,"users0")

if __name__ == '__main__':
    unittest.main()
