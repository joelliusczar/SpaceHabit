from SpaceUnitTest import SpaceUnitTest
from selenium import webdriver
import SpaceHabitServer
import threading
import cherrypy
import time
import requests
import DatabaseLayer

class Test_PlaygroundLoginJS(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    connection = DatabaseLayer.open_conn()
    connection.drop_database("spacetest")
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
    self.driver.get("http://127.0.0.1:8080/playground")
    self.input1 = self.driver.find_element_by_xpath("//input[@name='input1']")
    self.input2 = self.driver.find_element_by_xpath("//input[@name='input2']")
    self.input3 = self.driver.find_element_by_xpath("//input[@name='input3']")
    self.email1 = self.driver.find_element_by_xpath("//input[@name='email_input_1']")
    self.email2 = self.driver.find_element_by_xpath("//input[@name='email_input_2']")
    self.pw1 = self.driver.find_element_by_xpath("//input[@name='pw_input_1']")
    self.pw2 = self.driver.find_element_by_xpath("//input[@name='pw_input_2']")
    self.ship = self.driver.find_element_by_xpath("//input[@name='ship_input']")
    return super().setUp()

  def tearDown(self):
    self.driver.quit()
    return super().tearDown()

  def test_match(self):
    self.input1.send_keys("abcdefg")
    self.input2.send_keys("abcdefg")
    self.input3.send_keys("abcdefg")
    r = self.driver.execute_script("return ValidateInputsMatch('match');")
    self.assertTrue(r)

  def test_match_two(self):
    self.email1.send_keys("abcdefg")
    self.email2.send_keys("abcdefg")
    r = self.driver.execute_script("return ValidateInputsMatch('match_email');")
    self.assertTrue(r)

  def test_mismatch_two(self):
    self.email1.send_keys("abcdefg")
    self.email2.send_keys("abcd")
    r = self.driver.execute_script("return ValidateInputsMatch('match_email');")
    self.assertFalse(r)

  def test_mismatch_first(self):
    self.input1.send_keys("abcdefi")
    self.input2.send_keys("abcdefg")
    self.input3.send_keys("abcdefg")
    r = self.driver.execute_script("return ValidateInputsMatch('match');")
    self.assertFalse(r)

  def test_mismatch_last(self):
    self.input1.send_keys("abcdefg")
    self.input2.send_keys("abcdefg")
    self.input3.send_keys("abcdefj")
    r = self.driver.execute_script("return ValidateInputsMatch('match');")
    self.assertFalse(r)

  def test_match_empty(self):
    from selenium.common.exceptions import WebDriverException
    self.assertRaises(WebDriverException,lambda :self.driver.execute_script("return ValidateInputsMatch('empty');"))


  def test_caseSensitivity(self):
    self.input1.send_keys("abcdefg")
    self.input2.send_keys("Abcdefg")
    self.input3.send_keys("abcdefg")
    r = self.driver.execute_script("return ValidateInputsMatch('match',true);")
    self.assertFalse(r)
    r = self.driver.execute_script("return ValidateInputsMatch('match');")
    self.assertTrue(r)


if __name__ == '__main__':
  unittest.main()
