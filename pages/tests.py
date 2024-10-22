from django.test import SimpleTestCase #, TestCase for when using a DB

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_map_page_status_code(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)