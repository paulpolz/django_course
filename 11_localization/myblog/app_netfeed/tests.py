from django.test import TestCase
from django.urls import reverse
from app_netfeed.models import Feeds
from django.contrib.auth.models import User
from app_users.models import Profile

NUMBER_OF_FEEDS = 10
NUMBER_OF_USERS = 3
PASSWORD = 'QWERTy123'


class NetfeedListTests(TestCase):
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
                phone=f'+7999888665{i}',
                city='Moscow',
                about_me=f'Descripton_{i}'
            )
        
        for feed_index in range(NUMBER_OF_FEEDS):
            Feeds.objects.create(
                title=f'Feed number {feed_index}',
                author=Profile.objects.first(),
                text=f'Text of feed number {feed_index}'
            )

    def test_netfeed_list_access(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        
    def test_netfeed_detail_access(self):
        response = self.client.get(reverse('detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_netfeed_create_permission_access(self):
        # Не аутентифицированным пользователям доступ должен быть запрещен
        with self.assertRaises(PermissionError) as e:
            self.client.get(reverse('create'))
        self.assertEqual(e.exception.args[0], 'You are not logged in')

         # Аутентифицированный пользователь имеет доступ к созданию новостей
        self.client.login(username='user_1', password=PASSWORD)
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_netfeed_create_file_permission_access(self):
        # Не аутентифицированным пользователям доступ должен быть запрещен
        with self.assertRaises(PermissionError) as e:
            self.client.get(reverse('create_file'))
        self.assertEqual(e.exception.args[0], 'You are not logged in')

         # Аутентифицированный пользователь имеет доступ к созданию новостей
        self.client.login(username='user_1', password=PASSWORD)
        response = self.client.get(reverse('create_file'))
        self.assertEqual(response.status_code, 200)







