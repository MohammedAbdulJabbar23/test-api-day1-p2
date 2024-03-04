import unittest
import requests
from main import app
from models import User, Post

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"

    async def test_get_user(self):
        user = User(username="testuser")
        await user.save()  

        response = requests.get(f"{self.base_url}/users/{user.id}")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], user.id)
        self.assertEqual(data["username"], "testuser")

    async def test_get_posts(self):
        user = User(username="testuser")
        await user.save()  

        
        post1 = Post(title="Test Post 1", content="This is a test post 1", author=user, category="Test")
        await post1.save()  
        post2 = Post(title="Test Post 2", content="This is a test post 2", author=user, category="Test")
        await post2.save()  

        
        response = requests.get(f"{self.base_url}/posts")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

        post_ids = {post["id"] for post in data}
        self.assertIn(post1.id, post_ids)
        self.assertIn(post2.id, post_ids)

if __name__ == '__main__':
    unittest.main()
