from SpaceUnitTest import SpaceUnitTest
from datetime import datetime
import SpaceHabitServer
import DatabaseLayer
import cherrypy
import time
import requests
import json
import DatabaseTestSetupCleanup as dbHelp

class Test_MainPageRequests(SpaceUnitTest):
  
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

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()

  def test_checkIn(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"123456",'pw2':"123456",'shipName':"USS Enterprise"})
    timestamp = datetime.now().timestamp()*1000
    tzOffset = (datetime.now().timestamp() - datetime.utcnow().timestamp())/60
    r = s.get("http://127.0.0.1:8080/main/checkin",params={'utcElapsedTime': timestamp, 'utcOffset':tzOffset})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertIn('storyNotice',data)
    self.assertIn('zoneNotice',data)
    self.assertIn('zonePrompt',data)

  def test_disable_popups(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"123456",'pw2':"123456",'shipName':"USS Enterprise"})
    r = s.get("http://127.0.0.1:8080/main/disable_popups")
    self.assertEqual(r.status_code,200)

if __name__ == '__main__':
    unittest.main()
