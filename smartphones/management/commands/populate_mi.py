from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ------- Xiaomi BRAND -------
        xiaomi, created = Brand.objects.get_or_create(
            name="Xiaomi",
            slug="xiaomi",
            image="smartphones/Xiaomi-logo.png"
        )

        # ------- PHONE 1 -------
        redmi_note_14pro, created = Phone.objects.get_or_create(
            brand=xiaomi,
            name="Redmi Note 14 Pro",
            defaults={"image": "smartphones/Xiaomi/Redmi-note-14-Pro.png"}
        )

        Overview.objects.create(phone=redmi_note_14pro, text="Display: 6.7 AMOLED, 120Hz")
        Overview.objects.create(phone=redmi_note_14pro, text="Chipset: Snapdragon 7s Gen 2")
        Overview.objects.create(phone=redmi_note_14pro, text="RAM / Storage: 8GB / 256GB")

        KeySpec.objects.create(phone=redmi_note_14pro, text="Camera: 200MP Samsung HP3")
        KeySpec.objects.create(phone=redmi_note_14pro, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=redmi_note_14pro, text="Refresh Rate: 120Hz")

        # ------- PHONE 2 -------
        xiaomi_14, created = Phone.objects.get_or_create(
            brand=xiaomi,
            name="Xiaomi 14",
            defaults={"image": "smartphones/Xiaomi/Xiaomi-14.png"}
        )

        Overview.objects.create(phone=xiaomi_14, text="Display: 6.36 AMOLED, 120Hz")
        Overview.objects.create(phone=xiaomi_14, text="Chipset: Snapdragon 8 Gen 3")
        Overview.objects.create(phone=xiaomi_14, text="RAM / Storage: 12GB / 512GB")

        KeySpec.objects.create(phone=xiaomi_14, text="Camera: 50MP Leica, Summilux lens")
        KeySpec.objects.create(phone=xiaomi_14, text="Battery: 4610 mAh")
        KeySpec.objects.create(phone=xiaomi_14, text="Refresh Rate: 120Hz")

        # ------- PHONE 3 -------
        xiaomi_14_civi, created = Phone.objects.get_or_create(
            brand=xiaomi,
            name="Xiaomi 14 Civi",
            defaults={"image": "smartphones/Xiaomi/Xiaomi-14-civi.png"}
        )

        Overview.objects.create(phone=xiaomi_14_civi, text="Display: 6.55 AMOLED")
        Overview.objects.create(phone=xiaomi_14_civi, text="Chipset: Snapdragon 8 Gen 3")
        Overview.objects.create(phone=xiaomi_14_civi, text="RAM / Storage: 12GB / 256GB")

        KeySpec.objects.create(phone=xiaomi_14_civi, text="Camera: 50MP Sony LYT800")
        KeySpec.objects.create(phone=xiaomi_14_civi, text="Battery: 4700 mAh")
        KeySpec.objects.create(phone=xiaomi_14_civi, text="Refresh Rate: 120Hz")

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))