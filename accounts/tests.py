from django.test import TestCase
from django.contrib.auth import get_user_model


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
