from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        oneplus, created = Brand.objects.get_or_create(
            name="Oneplus",
            slug="oneplus",
            image="smartphones/oneplus.png"
        )

        # ------- PHONE 1 -------
        nord_5, created = Phone.objects.get_or_create(
            brand=oneplus,
            name="Oneplus NORD 5",
            defaults={"image": "smartphones/oneplus/NORD-5.webp"}
        )

        Overview.objects.create(phone=nord_5, text="Display: 6.74 AMOLED, 120Hz")
        Overview.objects.create(phone=nord_5, text="Chipset: Snapdragon 7+ Gen 2")
        Overview.objects.create(phone=nord_5, text="RAM / Storage: 8GB / 128GB")

        KeySpec.objects.create(phone=nord_5, text="Camera: 50MP Sony IMX890")
        KeySpec.objects.create(phone=nord_5, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=nord_5, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        oneplus_13, created = Phone.objects.get_or_create(
            brand=oneplus,
            name="OnePlus 13",
            defaults={"image": "smartphones/oneplus/oneplus-13.png"}
        )

        Overview.objects.create(phone=oneplus_13, text="Display: 6.8 LTPO AMOLED")
        Overview.objects.create(phone=oneplus_13, text="Chipset: Snapdragon 8 Gen 4")
        Overview.objects.create(phone=oneplus_13, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=oneplus_13, text="Camera: 50MP + 48MP + 50MP")
        KeySpec.objects.create(phone=oneplus_13, text="Battery: 5500 mAh")
        KeySpec.objects.create(phone=oneplus_13, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        oneplus_15, created = Phone.objects.get_or_create(
            brand=oneplus,
            name="OnePlus 15",
            defaults={"image": "smartphones/oneplus/oneplus-15.jpg"}
        )

        Overview.objects.create(phone=oneplus_15, text="Display: 6.8 AMOLED, 120Hz")
        Overview.objects.create(phone=oneplus_15, text="Chipset: Snapdragon 8 Gen 5")
        Overview.objects.create(phone=oneplus_15, text="RAM / Storage: 12GB / 512GB")

        KeySpec.objects.create(phone=oneplus_15, text="Camera: 50MP triple")
        KeySpec.objects.create(phone=oneplus_15, text="Battery: 5800 mAh")
        KeySpec.objects.create(phone=oneplus_15, text="Refresh Rate: 120Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))