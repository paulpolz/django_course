from django.test import TestCase
from django.urls import reverse
from app_catalog.models import Store, Category, Item
import random

NUMBER_OF_STORES = 10
NUMBER_OF_CATEGORIES = 5
NUMBER_OF_ITEMS = 100


class AppCatalogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        
    def test_store_list_access(self):
        response = self.client.get(reverse('stores'))
        self.assertEqual(response.status_code, 200)