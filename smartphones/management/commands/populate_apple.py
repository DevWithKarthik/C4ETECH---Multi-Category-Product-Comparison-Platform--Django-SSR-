from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        apple, created = Brand.objects.get_or_create(
            name="Apple",
            slug="apple",
            image="smartphones/apple.png"
        )

        # ------- PHONE 1 -------
        apple_17, created = Phone.objects.get_or_create(
            brand=apple,
            name="iPhone 17 Pro Max",
            defaults={"image": "smartphones/apple/17-pro-max.webp"}
        )

        Overview.objects.create(phone=apple_17, text="Display: 6.9 OLED")
        Overview.objects.create(phone=apple_17, text="Chipset: A19 Pro")
        Overview.objects.create(phone=apple_17, text="RAM / Storage: 8GB / 256GB–1TB")

        KeySpec.objects.create(phone=apple_17, text="Camera: 48MP main, 48MP ultrawide, 12MP telephoto")
        KeySpec.objects.create(phone=apple_17, text="Battery: 4700 mAh")
        KeySpec.objects.create(phone=apple_17, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        apple_17_mini, created = Phone.objects.get_or_create(
            brand=apple,
            name="iPhone 17",
            defaults={"image": "smartphones/Apple/Apple_17.png"}
        )

        Overview.objects.create(phone=apple_17_mini, text="Display: 6.3 OLED 120Hz")
        Overview.objects.create(phone=apple_17_mini, text="Chipset: A19")
        Overview.objects.create(phone=apple_17_mini, text="RAM / Storage: 8GB / 128 / 512GB")

        KeySpec.objects.create(phone=apple_17_mini, text="Camera: Dual 48MP + 12MP")
        KeySpec.objects.create(phone=apple_17_mini, text="Battery: 4200 mAh")
        KeySpec.objects.create(phone=apple_17_mini, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        apple_air, created = Phone.objects.get_or_create(
            brand=apple,
            name="iPhone Air",
            defaults={"image": "smartphones/apple/Apple-iPhone-Air.webp"}
        )

        Overview.objects.create(phone=apple_air, text="Display: 6.1 OLED")
        Overview.objects.create(phone=apple_air, text="Chipset: A18")
        Overview.objects.create(phone=apple_air, text="RAM / Storage: 6GB / 128 / 256GB")

        KeySpec.objects.create(phone=apple_air, text="Camera: 48MP + 12MP")
        KeySpec.objects.create(phone=apple_air, text="Battery: 4000 mAh")
        KeySpec.objects.create(phone=apple_air, text="Refresh Rate: 60 / 90Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))