from django.test import TestCase
from django.contrib.auth.models import User
from app_users.models import Profile
from django.urls import reverse

NUMBER_OF_USERS = 3
PASSWORD = 'QWERTy123'


class UsersRegisterTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(1, NUMBER_OF_USERS):
            user = User.objects.create(
                username=f'user_{i}',
                email=f'user_{i}@inbox.com',
            )
            user.set_password(PASSWORD)
            user.save()

            Profile.objects.create(
                user_login_id=user.id,
                birth_date='1995-01-01',
                phone=f'+7999888665{i}',
                city='Moscow'
            )
        
    def test_register_access(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_access(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_correct_auth(self):
        password = User.objects.filter(id=1).values('password')[0]['password']
        response = self.client.post(reverse('login'), {'username': 'user_1', 'password': password})
        self.assertEqual(response.status_code, 200)

    def test_logout_acceess(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)