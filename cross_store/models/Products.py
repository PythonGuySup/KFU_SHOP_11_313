from django.db import models
from .Category import Category


class Products(models.Model):
    CHOICES_BRAND = (
    ('love_moschino', 'Love Moschino'),
    ('hugo', 'HUGO'),
    ('calvin_klein', 'Calvin Klein'),
    ('nike', 'Nike'),
    ('adidas', 'Adidas'),
    ('vans', 'Vans'),
    ('converse', 'Converse'),
    ('new_balance', 'New Balance'),
    ('puma', 'Puma'),
    ('reebok', 'Reebok'),
    ('asics', 'ASICS'),
    ('jordan_brand', 'Jordan Brand'),
    ('fila', 'Fila'),
    ('salomon', 'Salomon'),
    ('hoka_one_one', 'Hoka One One'),
    ('saucony', 'Saucony'),
    ('brooks', 'Brooks'),
    ('under_armour', 'Under Armour'),
    ('on_running', 'On Running'),
    ('mizuno', 'Mizuno'),
    ('skechers', 'Skechers'),
    ('merrell', 'Merrell'),
    ('timberland', 'Timberland'),
    ('palladium', 'Palladium'),
    ('superga', 'Superga'),
    ('veja', 'Veja'),
    ('allbirds', 'Allbirds'),
    ('apl', 'APL'),
    ('common_projects', 'Common Projects'),
    ('golden_goose', 'Golden Goose'),
    ('koio', 'Koio'),
    ('axel_arigato', 'Axel Arigato'),
    ('off_white', 'Off-White'),
    ('balenciaga', 'Balenciaga'),
    ('gucci', 'Gucci'),
    ('louis_vuitton', 'Louis Vuitton'),
    ('prada', 'Prada'),
    ('saint_laurent', 'Saint Laurent'),
    ('yeezy', 'Yeezy'),
    ('fear_of_god', 'Fear of God'),
    ('amiri', 'Amiri'),
    ('rick_owens', 'Rick Owens'),
    ('maison_margiela', 'Maison Margiela'),
    ('hermes', 'Hermès'),
    ('fendi', 'Fendi'),
    ('marc_o\'polo', 'Marc O\'Polo'),
    ('месть', 'Месть'),
    ('sigma', 'Sigma'),
    ('ASH', 'ASH'),
    ('Guess', 'Guess'),
    ('vic_matie', 'Vic Matie'),
    ('tommy_hilfiger', 'Tommy Hilfiger'),
    ('steve_madden', 'Steve Madden'),
    ('polo_ralph_lauren', 'POLO RALPH LAUREN'),
    ('napapijri', 'NAPAPIJRI'),
)


    name = models.CharField(max_length=60, blank=True, null=True)
    brand = models.CharField(max_length=60, choices=CHOICES_BRAND)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='assets/img/preview/shop/', blank=True, null=True)

    @staticmethod   
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()
