from pickle import FALSE
import secrets

class Config:
  SECRET_KEY = secrets.token_hex(255) #creates app's secret key
  FLASK_COVERAGE = True #Sets Coverage for unit testing and for testing coverage


class DevelopmentConfig(Config):
  DEBUG = True #enables debug mode

class ProductionConfig(Config):
  DEBUG = False #enables debug mode
  FLASK_COVERAGE = False

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig
}