from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        huawei, created = Brand.objects.get_or_create(
            name="Huawei",
            slug="huawei",
            image="smartphones/Huawei-Logo.png"
        )

        # ------- PHONE 1 -------
        huawei_60, created = Phone.objects.get_or_create(
            brand=huawei,
            name="Huawei Mate 60",
            defaults={"image": "smartphones/huawei/Huawei-mate-60.jpg"}
        )

        Overview.objects.create(phone=huawei_60, text="Display: 6.69 LTPO OLED, 120Hz")
        Overview.objects.create(phone=huawei_60, text="Chipset: Kirin 9000S")
        Overview.objects.create(phone=huawei_60, text="RAM / Storage: 12GB / 256–512GB")

        KeySpec.objects.create(phone=huawei_60, text="Camera: 50MP main, Sony IMX766")
        KeySpec.objects.create(phone=huawei_60, text="Battery: 4750 mAh")
        KeySpec.objects.create(phone=huawei_60, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        huawei_mate, created = Phone.objects.get_or_create(
            brand=huawei,
            name="Huawei Mate X (fold)",
            defaults={"image": "smartphones/huawei/Huawei-mate-X.avif"}
        )

        Overview.objects.create(phone=huawei_mate, text="Display: 7.8 Foldable OLED, 120Hz")
        Overview.objects.create(phone=huawei_mate, text="Chipset: Kirin 9000 series")
        Overview.objects.create(phone=huawei_mate, text="RAM / Storage: 12GB / 512GB")

        KeySpec.objects.create(phone=huawei_mate, text="Camera: 50MP main (IMX766)")
        KeySpec.objects.create(phone=huawei_mate, text="Battery: 4600 mAh")
        KeySpec.objects.create(phone=huawei_mate, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        huawei_pura, created = Phone.objects.get_or_create(
            brand=huawei,
            name="Huawei Pura 70",
            defaults={"image": "smartphones/huawei/pura-70.png"}
        )

        Overview.objects.create(phone=huawei_pura, text="Display: 6.76 OLED, 120Hz")
        Overview.objects.create(phone=huawei_pura, text="Chipset: Kirin 9010")
        Overview.objects.create(phone=huawei_pura, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=huawei_pura, text="Camera: 50MP main, OmniVision OV50H")
        KeySpec.objects.create(phone=huawei_pura, text="Battery: 5200 mAh")
        KeySpec.objects.create(phone=huawei_pura, text="Refresh Rate: 120Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))