from django.core.management.base import BaseCommand
from smartphones.models import Brand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        brands = [
            ("Samsung", "samsung", "smartphones/samsung.png"),
            ("Apple", "apple", "smartphones/apple.png"),
            ("Huawei", "huawei", "smartphones/Huawei-Logo.png"),
            ("iQOO", "iqoo", "smartphones/iQOO.jpg"),
            ("OnePlus", "oneplus", "smartphones/oneplus.png"),
            ("Realme", "realme", "smartphones/realme-logo.png"),
            ("Vivo", "vivo", "smartphones/vivo.webp"),
            ("Xiaomi", "xiaomi", "smartphones/Xiaomi-logo.png"),
        ]

        for name, slug, img in brands:
            Brand.objects.get_or_create(name=name, slug=slug, image=img)

        self.stdout.write(self.style.SUCCESS("Brands populated successfully!"))
