from SpaceUnitTest import SpaceUnitTest
import SpaceHabitServer
import DatabaseLayer
import threading
import cherrypy
import time
import requests
import json
import DatabaseTestSetupCleanup as dbHelp


class Test_LoginSaveNewUserWithRequests(SpaceUnitTest):

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
    
    return super().setUp()

   


  def test_send_success(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"123456",'pw2':"123456",'shipName':"USS Enterprise"})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], True)
    

  def test_insert_user_missing_param(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"123456",'pw2':"123456"})
    self.assertEqual(r.status_code,404)


  def test_send_missing_input2_pw1_pw2(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"",'pw1':"",'pw2':"",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)


  def test_send_missing_pw(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"",'pw2':"",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)

  def test_send_taken_email(self):
    dbHelp.insert_one_user()
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"a@b.c",'pw1':"123456",'pw2':"123456",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)

  def test_send_mismatched_email(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"b@c.d",'pw1':"123456",'pw2':"123456",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)

  def test_send_bad_pw(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"b@c.d",'pw1':"123",'pw2':"123",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)

  def test_send_mismatched_pw(self):
    s = requests.Session()
    r = s.post("http://127.0.0.1:8080/login/save_new_user/",params={'email1':"a@b.c",
          'email2':"b@c.d",'pw1':"123456",'pw2':"abcdef",'shipName':""})
    self.assertEqual(r.status_code,200)
    data = json.loads(r.text)
    self.assertEqual(data['success'], False)


if __name__ == '__main__':
  unittest.main()
