from datetime import datetime
from peewee import *
from flask import current_app
from playhouse.shortcuts import model_to_dict
from app import db as mydb
#creating database connection instance


class TimelinePost(Model):
  name = CharField()
  email = CharField()
  content = TextField()
  created_at = DateTimeField(default=datetime.utcnow())

  class Meta:
    database = mydb

  def to_json(self):
    return model_to_dict(self);

#TODO: abstract this logic into a context cli function to create all tables, it will be very helpful when deploying
# mydb.connect();
# mydb.create_tables([TimelinePost])


