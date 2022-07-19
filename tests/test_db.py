import unittest
from peewee import *

from app.models import TimelinePost

MODELS=[TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()
    def test_timeline_post(self):
        first_post=TimelinePost.create(name='John Doe', 
        email='gabrielaj.4.f@gmail.com', content='Hello world, I\'m Gaby')
        assert first_post.id == 1

        second_post=TimelinePost.create(name='Jazmin Espinoza', 
        email='gabrielaj.4.f@example.com', content='Hello world, I\'m Jazmin')
        assert second_post.id == 2

        
