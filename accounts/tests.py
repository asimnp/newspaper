from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserManagerTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model()

    def test_create_user(self):
        user = self.user.objects.create_user(
            username="test", email="test@email.com", password="random-123"
        )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        super_user = self.user.objects.create_superuser(
            username="admin", email="admin@email.com", password="random-123"
        )
        self.assertEqual(super_user.username, "admin")
        self.assertEqual(super_user.email, "admin@email.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)


class SignUpViewTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

        response = self.client.post(
            reverse("signup"),
            {
                "username": "test1",
                "email": "test1@email.com",
                "password1": "random-123",
                "password2": "random-123",
            },
        )
        self.assertRedirects(response, reverse("login"), status_code=302)
        new_user = get_user_model().objects.last()
        self.assertEqual(new_user.username, "test1")
        self.assertEqual(new_user.email, "test1@email.com")
