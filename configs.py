import secrets
import os

from sqlalchemy import true

class Config:
  SECRET_KEY = secrets.token_hex(255) #creates app's secret key
  FLASK_COVERAGE = True #Sets Coverage for unit testing and for testing coverage
  DB_URL=os.environ.get('DB_URL', '')
  MYSQL_HOST=os.environ.get('MYSQL_HOST', '')
  MYSQL_USER=os.environ.get('MYSQL_USER', '')
  MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD', '')
  MYSQL_DATABASE=os.environ.get('MYSQL_DATABASE', '')
  SQLALCHEMY_DATABASE_URI=f'mysql+mysqlconnector://{os.environ.get("MYSQL_USER", "")}:{os.environ.get("MYSQL_PASSWORD", "")}@{os.environ.get("MYSQL_HOST", "")}:3306/{os.environ.get("MYSQL_DATABASE", "")}'

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