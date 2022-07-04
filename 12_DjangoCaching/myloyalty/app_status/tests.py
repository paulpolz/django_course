from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app_users.models import Profile
from app_status.models import Bonus, Offer, Purchase
from app_catalog.models import Store, Category, Item
import random

NUMBER_OF_USERS = 3
PASSWORD = 'QWERTy123'

NUMBER_OF_BONUSES = 3
NUMBER_OF_OFFERS = 5
NUMBER_OF_PURCHASES = 100
NUMBER_OF_STORES = 10
NUMBER_OF_CATEGORIES = 5
NUMBER_OF_ITEMS = 100


class AppStatusTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Users
        for user_index in range(NUMBER_OF_USERS):
            user=User.objects.create(
                username=f'user_{user_index}',
                email=f'user_{user_index}@inbox.com',
            )
            user.set_password(PASSWORD)
            user.save()

            Profile.objects.create(
                user_login_id=user.id,
                birth_date='1995-01-01',
                phone=f'+7999888665{user_index}',
                city='Moscow'
            )

        # Catalog
        for store_index in range(NUMBER_OF_STORES):
            Store.objects.create(
                name=f'Store Name {store_index}',
                city=f'Store City {store_index}',
                street=f'Store Street {store_index}',
                building=f'Store Building {store_index}',
                office=f'Store Office {store_index}'
            )

        for category_index in range(NUMBER_OF_CATEGORIES):
            Category.objects.create(
                name=f'Category Name {category_index}'
            )
        
        for item_index in range(NUMBER_OF_ITEMS):
            Item.objects.create(
                title=f'Store Title {item_index}',
                store=Store.objects.order_by('?').first(),
                category=Category.objects.order_by('?').first(),
                price=random.uniform(500, 1000)
            )

        # Status
        for bonus_index in range(NUMBER_OF_BONUSES):
            Bonus.objects.create(
                user=User.objects.get(username=f'user_{bonus_index}'),
                balance=random.uniform(500, 1000)
            )
        
        for offer_index in range(NUMBER_OF_OFFERS):
            offers = Offer.objects.create(
                title=f'Offer Title {offer_index}',
                subtitle=f'Offer SubTitle {offer_index}',
                is_special_offer=random.getrandbits(1),
                is_promo_event=random.getrandbits(1)
            )
            offers.store.set([Store.objects.order_by('?').first()])
            offers.save()

        for purchase_index in range(NUMBER_OF_PURCHASES):
            purchases = Purchase.objects.create(
                user=User.objects.order_by('?').first(),
                store=Store.objects.order_by('?').first(),
                category=Category.objects.order_by('?').first(),
                item=Item.objects.order_by('?').first()
            )
            purchases.offer_used.set([Offer.objects.order_by('?').first()])
            purchases.save()

    def test_account_permission_access(self):
        # Не аутентифицированным пользователям доступ должен быть запрещен
        with self.assertRaises(PermissionError) as e:
            self.client.get(reverse('account'))
        self.assertEqual(e.exception.args[0], 'You are not logged in')

        # Аутентифицированный пользователь имеет доступ к созданию новостей
        username = Bonus.objects.order_by('?').first().user
        self.client.login(username=username, password=PASSWORD)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    