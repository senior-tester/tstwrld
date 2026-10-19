from django.test import TestCase
from django.urls import reverse


class DirtyStringsIndexTests(TestCase):
    def test_dirty_strings_index_get_returns_200(self):
        response = self.client.get("/dirty-strings/")
        self.assertEqual(response.status_code, 200)

    def test_dirty_strings_index_uses_correct_template(self):
        response = self.client.get("/dirty-strings/")
        self.assertTemplateUsed(response, "dirty_strings/index.html")

    def test_dirty_strings_index_renders_heading(self):
        response = self.client.get("/dirty-strings/")
        self.assertContains(response, "Special & Dirty Strings")

    def test_dirty_strings_index_extends_base_shell(self):
        response = self.client.get("/dirty-strings/")
        content = response.content.decode()

        self.assertIn("QA Toolkit", content)
        self.assertIn('href="/bva/"', content)
        self.assertIn('href="/dirty-strings/"', content)