from django.test import TestCase
from django.urls import reverse


class BvaIndexTests(TestCase):
    def test_bva_index_get_returns_200(self):
        response = self.client.get("/bva/")
        self.assertEqual(response.status_code, 200)

    def test_bva_index_uses_correct_template(self):
        response = self.client.get("/bva/")
        self.assertTemplateUsed(response, "bva/index.html")

    def test_bva_index_renders_heading(self):
        response = self.client.get("/bva/")
        self.assertContains(response, "Boundary Values (BVA)")

    def test_bva_index_extends_base_shell(self):
        response = self.client.get("/bva/")
        content = response.content.decode()

        self.assertIn("QA Toolkit", content)
        self.assertIn('href="/bva/"', content)
        self.assertIn('href="/dirty-strings/"', content)