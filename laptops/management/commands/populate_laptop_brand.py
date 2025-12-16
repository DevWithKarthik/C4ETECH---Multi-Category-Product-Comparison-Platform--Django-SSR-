from django.core.management.base import BaseCommand
from laptops.models import BrandLaptop

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        brands = [
            ("Dell", "dell", "laptops/dell-logo.png"),
            ("Acer", "acer", "laptops/acer-logo.png"),
            ("Asus", "asus", "laptops/asus-logo.png"),
            ("HP", "hp", "laptops/HP-Logo.png"),
            ("Lenovo", "lenovo", "laptops/Lenovo-Logo.png"),
            ("Apple", "apple", "laptops/apple.png")
        ]

        for name, slug, img in brands:
            BrandLaptop.objects.get_or_create(name=name, slug=slug, image=img)

        self.stdout.write(self.style.SUCCESS("Brands populated successfully!"))