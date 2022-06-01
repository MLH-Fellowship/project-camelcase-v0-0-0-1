from flask import Flask
from configs import config

def create_app(config_profile: str):
    #creates app instance
    app = Flask(__name__)
    app.config.from_object(config[config_profile])

    #loads the view(s)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #returns app instance
    return app
