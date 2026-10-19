from django.test import TestCase
from django.urls import reverse, resolve


class RootRedirectTests(TestCase):
    def test_root_redirects_to_bva(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/bva/")

        followed = self.client.get("/", follow=True)
        self.assertEqual(followed.status_code, 200)
        self.assertTemplateUsed(followed, "bva/index.html")

    def test_bva_and_dirty_strings_return_200(self):
        response_bva = self.client.get("/bva/")
        self.assertEqual(response_bva.status_code, 200)

        response_ds = self.client.get("/dirty-strings/")
        self.assertEqual(response_ds.status_code, 200)

    def test_nonexistent_path_returns_404(self):
        response = self.client.get("/nonexistent/")
        self.assertEqual(response.status_code, 404)