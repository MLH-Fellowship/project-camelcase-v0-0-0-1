from . import api_v1
from app import db



@api_v1.before_request
def before_request():
  # print('Openning db connection')
  db.connect()


@api_v1.after_request
def after_request(response):
  # print('Closing db connection')
  db.close()
  return response;