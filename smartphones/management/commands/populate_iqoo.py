from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        iqoo, created = Brand.objects.get_or_create(
            name="iQOO",
            slug="iqoo",
            image="smartphones/iQOO.jpg"
        )

        # ------- PHONE 1 -------
        iqoo_13, created = Phone.objects.get_or_create(
            brand=iqoo,
            name="iQOO 13",
            defaults={"image": "smartphones/iQOO/iqoo-13.png"}
        )

        Overview.objects.create(phone=iqoo_13, text="Display: 6.78 AMOLED, 144Hz")
        Overview.objects.create(phone=iqoo_13, text="Chipset: Snapdragon 8 Gen 3")
        Overview.objects.create(phone=iqoo_13, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=iqoo_13, text="Camera: 50MP main, Samsung GN5")
        KeySpec.objects.create(phone=iqoo_13, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=iqoo_13, text="Refresh Rate: 144Hz")

        # ------- PHONE 2 -------
        iqoo_15, created = Phone.objects.get_or_create(
            brand=iqoo,
            name="iQOO 15",
            defaults={"image": "smartphones/iQOO/iqoo-15.png"}
        )

        Overview.objects.create(phone=iqoo_15, text="Display: 6.78 AMOLED")
        Overview.objects.create(phone=iqoo_15, text="Chipset: Snapdragon 8 Gen 4")
        Overview.objects.create(phone=iqoo_15, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=iqoo_15, text="Camera: 50MP main (GN5)")
        KeySpec.objects.create(phone=iqoo_15, text="Battery: 5100 mAh")
        KeySpec.objects.create(phone=iqoo_15, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        iqoo_neo_10, created = Phone.objects.get_or_create(
            brand=iqoo,
            name="iQOO Neo 10 Pro",
            defaults={"image": "smartphones/iQOO/iqoo-neo10-pro.png"}
        )

        Overview.objects.create(phone=iqoo_neo_10, text="Display: 6.78 AMOLED, 120Hz")
        Overview.objects.create(phone=iqoo_neo_10, text="Chipset: Snapdragon 8s Gen 3")
        Overview.objects.create(phone=iqoo_neo_10, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=iqoo_neo_10, text="Camera: 50MP Sony IMX920")
        KeySpec.objects.create(phone=iqoo_neo_10, text="Battery: 5500 mAh")
        KeySpec.objects.create(phone=iqoo_neo_10, text="Refresh Rate: 120Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))