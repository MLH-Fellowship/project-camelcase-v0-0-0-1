from app import create_app
import os
from app import db
from app.models import TimelinePost
import click

app = create_app(config_profile=os.getenv('FLASK_CONFIG') or 'development')

@app.shell_context_processor
def make_shell_context():
  print('making context')
  return dict(db=db, app=app, TimelinePost=TimelinePost)

@app.cli.command()
def deploy():
  print('Deploying db')
  db.connect();
  db.create_tables([TimelinePost])

@app.cli.command()
def test():
  import unittest
  # print(test_names)
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(test=tests)
  # sys.exit(not result.wasSuccessful())
  