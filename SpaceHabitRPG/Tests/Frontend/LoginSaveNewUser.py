from SpaceUnitTest import SpaceUnitTest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SpaceHabitServer
import threading
import cherrypy
import time
import requests
import DatabaseTestSetupCleanup as dbHelp


class Test_LoginSaveNewUser(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    import DatabaseLayer
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
    self.modal = self.driver.find_element_by_id("new_user_box")
    self.loginEmail = self.driver.find_element_by_xpath("//input[@name='input_login']")
    self.loginPw = self.driver.find_element_by_xpath("//input[@name='login_pw']")
    self.loginButton = self.driver.find_element_by_xpath("//button[@name='btnLogin']")
    return super().setUp()


  def tearDown(self):
    dbHelp.clean_up()
    self.driver.quit()
    return super().tearDown()


  def open_new_user_box(self):
    clickElem = self.driver.find_element_by_id("create_account")
    clickElem.click()

  def test_create_new_user(self):
    self.open_new_user_box()
    self.input1.send_keys("a@b.c")
    self.input2.send_keys("a@b.c")
    self.pw1.send_keys("123456")
    self.pw2.send_keys("123456")
    self.driver.find_element_by_xpath("//button[@name='save_user']").click()
    WebDriverWait(self.driver,10).until(EC.title_is("Space Habit Frontier!"))
    self.assertEqual(self.driver.title,"Space Habit Frontier!")

  def test_login(self):
    from selenium.common.exceptions import TimeoutException
    dbHelp.insert_test_user()
    self.loginEmail.send_keys("a@b.c")
    self.loginPw.send_keys("123456")
    self.loginButton.click()
    WebDriverWait(self.driver,10).until(EC.title_is("Space Habit Frontier!"))
    self.assertEqual(self.driver.title,"Space Habit Frontier!")
    self.driver.get("http://127.0.0.1:8080/login")
    self.assertRaises(TimeoutException,lambda :WebDriverWait(self.driver,5).until(EC.title_is("Login to Space Habit Frontier")))

  

if __name__ == '__main__':
  unittest.main()
