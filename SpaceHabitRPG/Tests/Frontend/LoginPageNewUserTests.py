from SpaceUnitTest import SpaceUnitTest
from selenium import webdriver
import SpaceHabitServer
import threading
import cherrypy
import time
import requests
import DatabaseLayer
import DatabaseTestSetupCleanup as dbHelp

class Test_LoginPageNewUserTests(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    dbHelp.clean_up()
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
    self.open_new_user_box()
    self.input1 = self.driver.find_element_by_xpath("//input[@name='email_input_1']")
    self.input2 = self.driver.find_element_by_xpath("//input[@name='email_input_2']")
    self.pw1 = self.driver.find_element_by_xpath("//input[@name='pw_input_1']")
    self.pw2 = self.driver.find_element_by_xpath("//input[@name='pw_input_2']")
    self.modal = self.driver.find_element_by_id("new_user_box")
    return super().setUp()


  def tearDown(self):
    dbHelp.clean_up()
    self.driver.quit()
    return super().tearDown()


  def open_new_user_box(self):
    clickElem = self.driver.find_element_by_id("create_account")
    clickElem.click()


  def test_bad_email(self):
    self.input1.send_keys("aaaa")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertTrue(elem.is_displayed())

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


  def test_taken_email(self):
    dbHelp.insert_one_test_login()
    self.input1.send_keys("a@b.c")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())


  def test_good_email(self):
    self.input1.send_keys("a@b.c")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())


  def test_mismatched_email(self):
    self.input1.send_keys("a@b.c")
    self.input2.send_keys("b@c.d")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())


  def test_bad_pw(self):
    self.pw1.click()
    self.pw1.send_keys("123")
    
    self.modal.click()
    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())

  def test_mismatch_pw(self):
    self.pw1.send_keys("123456")

    self.pw2.send_keys("abcded")
    self.modal.click()

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
    self.assertTrue(elem.is_displayed())


  def test_bad_then_good_email(self):
    self.input1.send_keys("aaaa")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertTrue(elem.is_displayed())

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

    self.input1.send_keys("a@b.c")
    self.modal.click()

    elem = self.driver.find_element_by_id("bad_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("taken_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_email")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("good_email")
    self.assertTrue(elem.is_displayed())

    elem = self.driver.find_element_by_id("short_pw")
    self.assertFalse(elem.is_displayed())

    elem = self.driver.find_element_by_id("mismatched_pw")
    self.assertFalse(elem.is_displayed())

if __name__ == '__main__':
  unittest.main()
