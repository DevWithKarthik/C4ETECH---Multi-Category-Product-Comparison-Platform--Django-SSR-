from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Apple BRAND -------
        realme, created = Brand.objects.get_or_create(
            name="Realme",
            slug="realme",
            image="smartphones/realme-logo.png"
        )

        # ------- PHONE 1 -------
        realme_15, created = Phone.objects.get_or_create(
            brand=realme,
            name="Realme 15 Pro",
            defaults={"image": "smartphones/realme/realme-15pro.png"}
        )

        Overview.objects.create(phone=realme_15, text="Display: 6.7 AMOLED, 120Hz")
        Overview.objects.create(phone=realme_15, text="Chipset: Snapdragon 7s Gen 2")
        Overview.objects.create(phone=realme_15, text="RAM / Storage: 8GB / 128GB")

        KeySpec.objects.create(phone=realme_15, text="Camera: 50MP Sony LYT600")
        KeySpec.objects.create(phone=realme_15, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=realme_15, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        realme_gt_7_pro, created = Phone.objects.get_or_create(
            brand=realme,
            name="Realme GT 7 Pro",
            defaults={"image": "smartphones/realme/realme-GT-7pro.webp"}
        )

        Overview.objects.create(phone=realme_gt_7_pro, text="Display: 6.78 AMOLED")
        Overview.objects.create(phone=realme_gt_7_pro, text="Chipset: Snapdragon 8 Gen 4")
        Overview.objects.create(phone=realme_gt_7_pro, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=realme_gt_7_pro, text="Camera: 50MP Sony IMX890")
        KeySpec.objects.create(phone=realme_gt_7_pro, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=realme_gt_7_pro, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        realme_gt_8_pro, created = Phone.objects.get_or_create(
            brand=realme,
            name="Realme GT 8 Pro",
            defaults={"image": "smartphones/realme/realme-gt-8pro.webp"}
        )

        Overview.objects.create(phone=realme_gt_8_pro, text="Display: 6.7 AMOLED, 1220p")
        Overview.objects.create(phone=realme_gt_8_pro, text="Chipset: Snapdragon 8 Gen 3")
        Overview.objects.create(phone=realme_gt_8_pro, text="RAM / Storage: 12GB")

        KeySpec.objects.create(phone=realme_gt_8_pro, text="Camera: 50MP Sony IMX966")
        KeySpec.objects.create(phone=realme_gt_8_pro, text="Battery: 5500 mAh")
        KeySpec.objects.create(phone=realme_gt_8_pro, text="Refresh Rate: 120Hz")
        
        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))