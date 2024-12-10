import unittest
from app import app

class LibraryAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_book(self):
        response = self.client.post("/books/", json={
            "title": "Sample Book",
            "author": "Author Name",
            "year": 2020,
            "genre": "Fiction"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_search_books(self):
        response = self.client.get("/books/search?q=Sample")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
