
import unittest
from urllib import response
from flask import current_app
from app import create_app, db


class BasicTests(unittest.TestCase):
  """ This unit test is mean to test basic parts of the app, checking that all endpoints respond with no error code 
      
  """
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.client = self.app.test_client()
  
  def tearDown(self):
    self.app_context.pop()

  def test_app_runs(self):
    self.assertFalse(current_app is None)

  def test_landing_page(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)