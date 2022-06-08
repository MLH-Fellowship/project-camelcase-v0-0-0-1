from app import create_app
import os

app = create_app(config_profile=os.getenv('FLASK_CONFIG') or 'development')