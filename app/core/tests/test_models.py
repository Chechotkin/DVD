"""Module disc

"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    ''' Cals desc '''

    def test_create_user_with_email_succ(self):
        """Test email one
        """
        email = 'test@ukr.net'
        password = 'test-pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normlize(self):
        """Email normalize
        """
        email = 'test@BIGCAPS.COM'
        user = get_user_model().objects.create_user(email, '123-123')

        self.assertEqual(user.email, email.lower())

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
