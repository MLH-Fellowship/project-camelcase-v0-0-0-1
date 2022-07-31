
import unittest
import os
os.environ['TESTING'] = 'true'
from tests import test_db


from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()


    def test_home(self):
        response = self.client.get("/gabby")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>  GABBY  </title>" in html

        # TODO Add more tests relating to the home page

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis

       
        test_db.TestTimelinePost.test_timeline_post(self)
        postResponse = self.client.get("/api/timeline_post")
        assert postResponse.status_code == 200
        assert postResponse.is_json
        jsonPost = postResponse.get_json()
        assert "timeline_posts" in jsonPost
        assert len(jsonPost["timeline_posts"]) == 2
        

        # TODO Add more tests relating to the timeline page

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Form submit width Fetch API</title>" in html


    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"name": "", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html


        #POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email":"john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html


        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

#POST request with malformed email
