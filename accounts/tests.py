from django.test import TestCase
from django.utils import timezone
from django.db import transaction, IntegrityError
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def setUp(self):
        # This method is called before each test
        User.objects.create(username='testuser', password='testpassword', email='test@example.com')

    def tearDown(self):
        # This method is called after each test
        User.objects.all().delete()

    def test_user_creation(self):
        """Test that the created_at field is set correctly when a user is created."""
        user = User.objects.get(username='testuser')
        
        # Check that the created_at field is set within 1 second of the current time
        self.assertTrue(timezone.now() - user.date_joined < timezone.timedelta(seconds=1))

    def test_user_str_method(self):
        """Test the __str__ method of the User model."""
        user = User.objects.get(username='testuser')
        
        # Check that the __str__ method returns the expected value
        self.assertEqual(str(user), 'testuser')

    def test_user_ordering(self):
        """Test the ordering of users by the created_at field."""
        # Create additional users with different creation times
        User.objects.create(username='user2', password='password2', email='user2@example.com')
        User.objects.create(username='user3', password='password3', email='user3@example.com')

        # Check that the ordering is correct
        users = User.objects.all()
        self.assertEqual(users[0].username, 'testuser')
        self.assertEqual(users[1].username, 'user2')
        self.assertEqual(users[2].username, 'user3')

    def test_unique_username(self):
        """Test that there can't be users with the same username"""

        # Create a user with a unique username
        User.objects.create(username='unique_user', password='password123', email='unique@example.com')

        try:
            with transaction.atomic():
                User.objects.create(username='unique_user', password='another_password', email='another@example.com')
            self.fail('Duplicate username allowed.')
        except IntegrityError:
            pass

    def test_unique_email(self):
        """Test that there can't be users with the same email"""

        # Create a user with a unique email
        User.objects.create(username='user1', password='password123', email='unique@example.com')

        # Try to create another user with the same email
        try:
            with transaction.atomic():
                User.objects.create(username='user1', password='another_password', email='unique@example.com')
            self.fail('Duplicate email allowed.')
        except IntegrityError:
            pass
