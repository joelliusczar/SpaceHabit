from SpaceUnitTest import SpaceUnitTest
from AuthenticationLayer import AuthenticationFields as fields
import AuthenticationLayer as auth
import EverywhereConstants as consts
import DatabaseTestSetupCleanup as dbHelp
import DatabaseLayer

class Test_AuthenticationLayerTests(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    return super().setUpClass()

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()

  def test_insert_new_user(self):
    result = auth.insert_new_user("a0@b.c","p","s")
    self.assertEqual(len(result),3)
    self.assertRaises(FileExistsError,lambda :auth.insert_new_user("a0@b.c","p","s"))

  def test_is_login_taken(self):
    t = auth.is_login_taken("a1@b.c")
    self.assertFalse(t)
    auth.insert_new_user("b1@c.d","p","s")
    t = auth.is_login_taken("b1@c.d")
    self.assertTrue(t)

  def test_authenticate_user(self):
    auth.insert_new_user("c3@d.e","p","s")
    result = auth.authenticate_user("d3@e.f","")
    self.assertEqual(len(result['messages']),1)
    self.assertEqual(result['messages'][0],"#bad_login")
    result = auth.authenticate_user("c3@d.e","123")
    self.assertEqual(len(result['messages']),1)
    self.assertEqual(result['messages'][0],"#bad_login_pw")
    result = auth.authenticate_user("c3@d.e","p")
    self.assertEqual(len(result['messages']),0)
    self.assertTrue(result['success'])

  def test_validate_email(self):
    auth.insert_new_user("a4@b.c","p","s")
    t = auth.validate_email("@@")
    self.assertFalse(t['success'])
    self.assertEqual(t['messages'][0],"#bad_email")
    t = auth.validate_email("a4@b.c")
    self.assertFalse(t['success'])
    self.assertEqual(t['messages'][0],"#taken_email")
    t = auth.validate_email("b4@c.d")
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
    t = auth.check_all_new_user_validations("a5@b.c","a5@b.c","123456","123456","ship")
    self.assertEqual(len(t),0)


  def test_safe_insert_new_user(self):
    id = auth.safe_insert_new_user("a","123")
    users = DatabaseLayer.get_table(fields.COLLECTION_NAME)
    user = users.find_one({consts.ID_KEY:id})
    self.assertIsNotNone(user)

if __name__ == '__main__':
  unittest.main()
