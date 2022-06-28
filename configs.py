import secrets
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  SECRET_KEY = secrets.token_hex(255) #creates app's secret key
  FLASK_COVERAGE = False #Sets Coverage for unit testing and for testing coverage
  DB_URL=os.getenv('DB_URL')
  MYSQL_HOST=os.getenv('MYSQL_HOST')
  MYSQL_USER=os.getenv('MYSQL_USER')
  MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
  MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')

class DevelopmentConfig(Config):
  DEBUG = True #enables debug mode
  SQLALCHEMY_TRACK_MODIFICATIONS=True

class ProductionConfig(Config):
  DEBUG = False #enables debug mode
  FLASK_COVERAGE = False

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig
}