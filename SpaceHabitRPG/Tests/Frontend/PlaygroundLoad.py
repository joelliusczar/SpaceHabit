from SpaceUnitTest import SpaceUnitTest
import SpaceHabitServer
import MockSetUp
import threading
import cherrypy
import time
from selenium import webdriver
import requests
import MockDataLoader
import MockDatabaseLayer
import SeleniumHelper

class Test_PlaygroundLoad(SpaceUnitTest):

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


    def test_load(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://127.0.0.1:8080/playground")
        self.assertEqual(driver.title,"Test Playground")
        driver.quit()

if __name__ == '__main__':
    unittest.main()