
import datetime 
from app import mydb
from peewee import * 

from playhouse.shortcuts import model_to_dict


class TimelinePost(Model):
        name = CharField()
        email = CharField()
        content = TextField()
        created_at = DateTimeField(default=datetime.datetime.now)

        def to_json(self):
            return model_to_dict(self)
            
        class Meta:
            database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])