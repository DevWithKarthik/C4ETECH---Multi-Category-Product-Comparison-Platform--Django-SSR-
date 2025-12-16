from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone, Overview, KeySpec

class Command(BaseCommand):

    
    help = "Populate the database with smartphone brands and models."

    def handle(self, *args, **kwargs):

        # -------- Delete old data safely --------
        Brand.objects.all().delete()
        Phone.objects.all().delete()
        Overview.objects.all().delete() 
        KeySpec.objects.all().delete()          

        # ------- Samsung BRAND -------
        samsung, created = Brand.objects.get_or_create(
            name="Samsung",
            slug="samsung",
            image="smartphones/samsung.png"
        )

        # ------- PHONE 1 -------
        s25_ultra, created = Phone.objects.get_or_create(
            brand=samsung,
            name="Samsung S25 Ultra",
            defaults={"image": "smartphones/samsung/S25-Ultra1.webp"}
        )

        Overview.objects.create(phone=s25_ultra, text="Display: 6.8 AMOLED")
        Overview.objects.create(phone=s25_ultra, text="Chipset: Snapdragon / Exynos")
        Overview.objects.create(phone=s25_ultra, text="RAM: 12GB")

        KeySpec.objects.create(phone=s25_ultra, text="Battery: 5000 mAh")
        KeySpec.objects.create(phone=s25_ultra, text="Camera: 200 MP")
        KeySpec.objects.create(phone=s25_ultra, text="OS: Android 15")

        # ------- PHONE 2 -------
        s25_fe, created = Phone.objects.get_or_create(
            brand=samsung,
            name="Samsung S25 FE",
            defaults={"image": "smartphones/samsung/S25-FE.avif"}
        )

        Overview.objects.create(phone=s25_fe, text="Display: 6.5 AMOLED")
        Overview.objects.create(phone=s25_fe, text="Chipset: Mid-range")
        Overview.objects.create(phone=s25_fe, text="RAM: 8GB")

        KeySpec.objects.create(phone=s25_fe, text="Battery: 4500 mAh")
        KeySpec.objects.create(phone=s25_fe, text="Camera: 64 MP")
        KeySpec.objects.create(phone=s25_fe, text="Price Tier: Mid")

        # ------- PHONE 3 -------
        s24, created = Phone.objects.get_or_create(
            brand=samsung,
            name="Samsung S24 Plus",
            defaults={"image": "smartphones/samsung/S24-plus.jpg"}
        )
    
        Overview.objects.create(phone=s24, text="Display: 6.7 AMOLED")
        Overview.objects.create(phone=s24, text="Chipset: Flagship lite")
        Overview.objects.create(phone=s24, text="RAM / Storage: 8GB / 256GB")

        KeySpec.objects.create(phone=s24, text="Battery: 4800 mAh")
        KeySpec.objects.create(phone=s24, text="Camera: 108 MP main")
        KeySpec.objects.create(phone=s24, text="Colors: Black, Silver, Blue")

        

        self.stdout.write(self.style.SUCCESS("Smartphone data populated successfully!"))
