from django.core.management.base import BaseCommand
from homeappliances.models import BrandHomeAppliances

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        brands = [
            ("Air Conditioner", "air-conditioner", "homeappliances/air-conditioner.png"),
            ("Refrigerator", "refrigerator", "homeappliances/fridge-image.jpg"),
            ("Washing Machine", "washing-machine", "homeappliances/washing-machine.png"),
            ("Television", "television", "homeappliances/Television.jpg"),
        ]

        for name, slug, img in brands:
            BrandHomeAppliances.objects.get_or_create(name=name, slug=slug, image=img)

        self.stdout.write(self.style.SUCCESS("Brands populated successfully!"))