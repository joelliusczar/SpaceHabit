from SpaceUnitTest import SpaceUnitTest
import SpaceHabitServer
import MockSetUp
import threading
import cherrypy
import time
from selenium import webdriver
import SeleniumHelper
import requests
import MockDataLoader



class Test_LoginPageTest(SpaceUnitTest):

    @classmethod
    def setUpClass(cls):
        MockSetUp.set_up_mock_db_connections()
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
        return super().setUp()

    def tearDown(self):
        import MockDatabaseLayer
        MockDatabaseLayer.clean_up()
        self.driver.quit()
        return super().tearDown()

    def test_initial_page_is_login(self):
        self.assertEqual(self.driver.current_url,"http://127.0.0.1:8080/login/")
        self.assertEqual(self.driver.title,"Login to Space Habit Frontier")
        
    def test_login_page_default_state(self):
        elem = self.driver.find_element_by_id("bad_login")
        self.assertFalse(elem.is_displayed())

        elem = self.driver.find_element_by_id("bad_login_pw")
        self.assertFalse(elem.is_displayed())

        elem = self.driver.find_element_by_id("new_user_box")
        self.assertFalse(elem.is_displayed())

        elem = self.driver.find_element_by_id("forgotten_pw_box")
        self.assertFalse(elem.is_displayed())

    def open_new_user_box(self):
        clickElem = self.driver.find_element_by_id("create_account")
        clickElem.click()

    def test_create_user_model_validation_is_clean(self):
        self.open_new_user_box()
        elem = self.driver.find_element_by_id("new_user_box")
        self.assertTrue(elem.is_displayed())

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





if __name__ == '__main__':
    unittest.main()