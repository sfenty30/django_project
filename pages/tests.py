from django.test import SimpleTestCase

class HomePageTest(simpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = sef.client.get("/")
        self.assertEqual(response.status_code, 200)

 class AboutPageView(simpleTestCase):
     def test_url_exist_at_correct_location(self):  
         response = self.client.get("about/")
         self.assertEqual(reponse.status_code, 200)