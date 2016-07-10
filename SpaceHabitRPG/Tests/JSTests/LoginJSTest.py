from SpaceUnitTest import SpaceUnitTest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SpaceHabitServer
import threading
import cherrypy
import time
import requests
import AuthenticationLayer
import DatabaseLayer
import DatabaseTestSetupCleanup as dbHelp

class Test_LoginJSTest(SpaceUnitTest):
  
  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    cls.server = SpaceHabitServer.HabitServer()
    cls.server.start()
    ticks = 0
    while cherrypy.engine.state != cherrypy.engine.states.STARTED:
      time.sleep(1)
      ticks += 1
      if ticks >= 10:
        raise TimeoutError("ran out of time")
    return super().setUpClass()

  @classmethod
  def tearDownClass(cls):
    dbHelp.clean_up()
    cls.server.stop()
    ticks = 0
    while cherrypy.engine.state != cherrypy.engine.states.STOPPED:
      time.sleep(1)
      ticks += 1
      if ticks >= 10:
        raise TimeoutError("ran out of time")
    return super().tearDownClass()

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(5)
    self.driver.get("http://127.0.0.1:8080")
    self.input1 = self.driver.find_element_by_xpath("//input[@name='email_input_1']")
    self.input2 = self.driver.find_element_by_xpath("//input[@name='email_input_2']")
    self.pw1 = self.driver.find_element_by_xpath("//input[@name='pw_input_1']")
    self.pw2 = self.driver.find_element_by_xpath("//input[@name='pw_input_2']")
    self.ship = self.driver.find_element_by_xpath("//input[@name='ship_input']")
    self.newUserModal = self.driver.find_element_by_id("new_user_box")
    self.pwModal = self.driver.find_element_by_id("forgotten_pw_box")
    return super().setUp()

  def tearDown(self):
    self.driver.quit()
    return super().tearDown()

  def open_new_user_box(self):
    clickElem = self.driver.find_element_by_id("create_account")
    clickElem.click()

  def test_clearNewAccountWindow(self):
    self.open_new_user_box()
    self.input1.send_keys("aaaaa")
    self.input2.send_keys("bbbbb")
    self.pw1.send_keys("cccc")
    self.pw2.send_keys("dddd")
    self.ship.send_keys("eeee")
    self.driver.execute_script("clearNewAccountWindow();")
    self.assertEqual(self.input1.get_attribute('value'),"")
    self.assertEqual(self.input2.get_attribute('value'),"")
    self.assertEqual(self.pw1.get_attribute('value'),"")
    self.assertEqual(self.pw2.get_attribute('value'),"")
    self.assertEqual(self.ship.get_attribute('value'),"")

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())


  def test_createAccountClick(self):
    elem = self.driver.find_element_by_id("new_user_box")
    self.assertFalse(elem.is_displayed())
    self.driver.execute_script("createAccountClick();")
    self.assertTrue(elem.is_displayed())


  def test_forgotPWClick(self):
    self.assertFalse(self.pwModal.is_displayed())
    self.driver.execute_script("forgotPWClick();")
    self.assertTrue(self.pwModal.is_displayed())


  def test_cancelAddClick(self):
    self.open_new_user_box()
    self.assertTrue(self.newUserModal.is_displayed())
    self.driver.execute_script("cancelAddClick();")
    self.assertFalse(self.newUserModal.is_displayed())


  def test_cancelForgotPassword(self):
    self.driver.find_element_by_id("forgot_pw").click()
    self.assertTrue(self.pwModal.is_displayed())
    self.driver.execute_script("cancelForgotPassword();")
    self.assertFalse(self.pwModal.is_displayed())


  def test_validateEmailAjaxSuccess(self):
    self.open_new_user_box()
    self.driver.execute_script(
      "validateNewEmailAjaxSuccess("
      "{'messages':['#bad_email'],'success':false});")

    elem = self.driver.find_element_by_id("bad_email")
    self.assertTrue(elem.is_displayed())

    self.driver.execute_script(
      "validateNewEmailAjaxSuccess("
      "{'messages':['#bad_email','#taken_email'],'success':false});")

    elem = self.driver.find_element_by_id("bad_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertTrue(elem.is_displayed())

    self.driver.execute_script(
      "validateNewEmailAjaxSuccess("
      "{'messages':['#good_email'],'success':true});")

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertTrue(elem.is_displayed())

  def test_loginAjaxSuccessSession(self):
    AuthenticationLayer.disableAuthenticationRedirects = True
    self.driver.execute_script("loginAjaxSuccess({'messages':[\"#bad_login\",\"#bad_login_pw\"],'success':false});")
    
    self.assertEqual(self.driver.title,"Login to Space Habit Frontier")
    elem = self.driver.find_element_by_id("bad_login")
    self.assertTrue(elem.is_displayed())
    elem = self.driver.find_element_by_id("bad_login_pw")
    self.assertTrue(elem.is_displayed())

    self.driver.execute_script("loginAjaxSuccess({'messages':[\"#bad_login_pw\"],'success':false});")
    
    self.assertEqual(self.driver.title,"Login to Space Habit Frontier")
    elem = self.driver.find_element_by_id("bad_login")
    self.assertFalse(elem.is_displayed())
    elem = self.driver.find_element_by_id("bad_login_pw")
    self.assertTrue(elem.is_displayed())

    self.driver.execute_script("loginAjaxSuccess({'messages':[],'success':true});")
    #WebDriverWait(self.driver,10).until(EC.title_is("Space Habit Frontier!"))
    self.assertEqual(self.driver.title,"Space Habit Frontier!")

  def test_onEmail2InputBlur(self):
    self.open_new_user_box()
    self.input1.send_keys("a@b.c")
    self.input2.send_keys("b@c.d")
    self.driver.execute_script("onEmail2InputBlur();")
    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertTrue(elem.is_displayed())
    self.input2.clear()
    self.input2.send_keys("a@b.c")
    self.assertEqual(self.input1.get_attribute('value'),self.input2.get_attribute('value'))
    self.driver.execute_script("onEmail2InputBlur();")
    self.assertFalse(elem.is_displayed())

  def test_onPw1InputBlur(self):
    self.open_new_user_box()
    self.pw1.send_keys("123")
    self.driver.execute_script("onPw1InputBlur();")
    elem = self.driver.find_element_by_id("short_pw")
    self.assertTrue(elem.is_displayed())
    self.pw1.clear()
    self.pw1.send_keys("123456")
    self.driver.execute_script("onPw1InputBlur();")
    self.assertFalse(elem.is_displayed())

  def test_onPw2InputBlur(self):
    self.open_new_user_box()
    self.pw1.send_keys("abcdef")
    self.pw2.send_keys("Abcdef")
    self.driver.execute_script("onPw2InputBlur();")
    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertTrue(elem.is_displayed())
    self.pw2.clear()
    self.pw2.send_keys("abcdef")
    self.assertEqual(self.pw1.get_attribute('value'),self.pw2.get_attribute('value'))
    self.driver.execute_script("onPw2InputBlur();")
    self.assertFalse(elem.is_displayed())


if __name__ == '__main__':
  unittest.main()
