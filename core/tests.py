from django.test import TestCase, override_settings
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


class SharedLayoutTests(TestCase):
    def _assert_shared_markers(self, response, expected_heading):
        content = response.content.decode()
        self.assertIn("QA Toolkit", content)
        self.assertIn("v0.1.0-alpha", content)
        self.assertIn("https://github.com/senior-tester/tstwrld", content)
        self.assertIn('href="/bva/"', content)
        self.assertIn('href="/dirty-strings/"', content)
        self.assertIn("All Pairs", content)
        self.assertIn("Coming in v0.2", content)
        self.assertIn("JSON/JWT Inspector", content)
        self.assertIn("aria-disabled", content)
        self.assertIn("pointer-events-none", content)
        self.assertIn(expected_heading, content)

    def test_bva_page_has_shared_layout(self):
        response = self.client.get("/bva/")
        self.assertEqual(response.status_code, 200)
        self._assert_shared_markers(response, "Boundary Values (BVA)")

    def test_dirty_strings_page_has_shared_layout(self):
        response = self.client.get("/dirty-strings/")
        self.assertEqual(response.status_code, 200)
        self._assert_shared_markers(response, "Special & Dirty Strings")


class ThemeMarkupTests(TestCase):
    def test_pre_paint_theme_script_present(self):
        response = self.client.get("/bva/")
        content = response.content.decode()

        self.assertIn("qa-theme", content)
        self.assertIn("prefers-color-scheme", content)
        self.assertIn('document.documentElement.classList.add("dark")', content)

    def test_theme_script_before_tailwind_cdn(self):
        response = self.client.get("/bva/")
        content = response.content.decode()

        theme_script_pos = content.find("qa-theme")
        tailwind_cdn_pos = content.find("cdn.tailwindcss.com")

        self.assertNotEqual(theme_script_pos, -1, "Theme script not found")
        self.assertNotEqual(tailwind_cdn_pos, -1, "Tailwind CDN not found")
        self.assertLess(theme_script_pos, tailwind_cdn_pos)

    def test_single_alpine_theme_controller_scope(self):
        response = self.client.get("/bva/")
        content = response.content.decode()

        occurrences = content.count('x-data="themeController()"')
        self.assertEqual(occurrences, 1)

    def test_no_cursor_not_allowed(self):
        response = self.client.get("/bva/")
        content = response.content.decode()

        self.assertNotIn("cursor-not-allowed", content)

    def test_root_redirects_instead_of_rendering_core_index(self):
        # core:index URL pattern exists but redirects to bva:index via RedirectView
        # Verify that visiting / redirects instead of rendering a core/index.html template
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/bva/")

        # Ensure no core/index.html template exists (would be rendered if not for RedirectView)
        from django.template.loader import select_template
        with self.assertRaises(Exception):
            select_template(["core/index.html"])