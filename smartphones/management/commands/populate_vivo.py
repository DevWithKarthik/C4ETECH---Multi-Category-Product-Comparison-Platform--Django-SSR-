from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        vivo, created = Brand.objects.get_or_create(
            name="Vivo",
            slug="vivo",
            image="smartphones/vivo.webp"
        )

        # ------- PHONE 1 -------
        vivo_v60, created = Phone.objects.get_or_create(
            brand=vivo,
            name="Vivo V60 Pro",
            defaults={"image": "smartphones/Vivo/Vivo-V60.webp"}
        )

        Overview.objects.create(phone=vivo_v60, text="Display: 6.7 AMOLED")
        Overview.objects.create(phone=vivo_v60, text="Chipset: Dimensity 8300")
        Overview.objects.create(phone=vivo_v60, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=vivo_v60, text="Camera: 50MP Sony LYT600")
        KeySpec.objects.create(phone=vivo_v60, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=vivo_v60, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        vivo_x_fold3, created = Phone.objects.get_or_create(
            brand=vivo,
            name="Vivo X Fold 3",
            defaults={"image": "smartphones/Vivo/Vivo-X-Fold3.jpg"}
        )

        Overview.objects.create(phone=vivo_x_fold3, text="Display: 7.85 foldable AMOLED")
        Overview.objects.create(phone=vivo_x_fold3, text="Chipset: Snapdragon 8 Gen 3")
        Overview.objects.create(phone=vivo_x_fold3, text="RAM / Storage: 12GB / 512GB")

        KeySpec.objects.create(phone=vivo_x_fold3, text="Camera: 50MP Sony IMX866")
        KeySpec.objects.create(phone=vivo_x_fold3, text="Battery: 5500 mAh")
        KeySpec.objects.create(phone=vivo_x_fold3, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        vivo_x300, created = Phone.objects.get_or_create(
            brand=vivo,
            name="Vivo X300",
            defaults={"image": "smartphones/Vivo/X300pro.jpg"}
        )

        Overview.objects.create(phone=vivo_x300, text="Display: 6.78 AMOLED")
        Overview.objects.create(phone=vivo_x300, text="Chipset: Snapdragon 8 Gen 4")
        Overview.objects.create(phone=vivo_x300, text="RAM / Storage: 16GB / 1TB")

        KeySpec.objects.create(phone=vivo_x300, text="Camera: 50MP Sony IMX989")
        KeySpec.objects.create(phone=vivo_x300, text="Battery: 5500 mAh")
        KeySpec.objects.create(phone=vivo_x300, text="Refresh Rate: 120Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))