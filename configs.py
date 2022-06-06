import secrets

class Config:
  SECRET_KEY = secrets.token_hex(255) #creates app's secret key
  FLASK_COVERAGE = True #Sets Coverage for unit testing and for testing coverage


class DevelopmentConfig(Config):
  DEBUG = True #enables debug mode


config = {
  'development': DevelopmentConfig
}