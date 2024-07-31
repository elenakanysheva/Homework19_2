from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'pk': 1, 'name': 'Одежда', 'description': 'Одежда для всей семьи'},
            {'pk': 2, 'name': 'Обувь', 'description': 'Обувь для всей семьи'},
            {'pk': 3, 'name': 'Дом', 'description': 'Товары для дома'}
        ]



        product_for_create = []
        category_for_create = []

        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Платье женское', 'category': Category.objects.get(pk=1)},
            {'name': 'Брюки мужские', 'category': Category.objects.get(pk=1)},
            {'name': 'Туфли женские', 'category': Category.objects.get(pk=2)},
            {'name': 'Ваза', 'category': Category.objects.get(pk=3)},
            {'name': 'Плед', 'category': Category.objects.get(pk=3)}

        ]

        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
