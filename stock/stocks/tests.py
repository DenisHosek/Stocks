from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class IndexPageTestCase(TestCase):
    def test_displayIndex(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_displayreg(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_crate_form(self):
        username = 'franta'
        password = '1234DFE56778'
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(
            reverse('register'),
            {'username': username,
            'password1': password,
            'password2': password
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username=username).exists())