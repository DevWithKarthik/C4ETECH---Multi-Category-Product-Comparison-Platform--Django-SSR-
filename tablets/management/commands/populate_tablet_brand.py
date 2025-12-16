from django.core.management.base import BaseCommand
from tablets.models import BrandTablets

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        brands = [
            ("iPad", "ipad", "tablets/apple.png"),
            ("Lenovo", "lenovo", "tablets/Lenovo-Logo.png"),
            ("Samsung", "samsung", "tablets/samsung.png"),
            ("Xiaomi", "xiaomi", "tablets/Xiaomi-logo.png")
        ]

        for name, slug, img in brands:
            BrandTablets.objects.get_or_create(name=name, slug=slug, image=img)

        self.stdout.write(self.style.SUCCESS("Brands populated successfully!"))