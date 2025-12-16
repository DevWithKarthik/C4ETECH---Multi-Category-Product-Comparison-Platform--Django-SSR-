from django.core.management.base import BaseCommand
from smartphones.models import Phone, KeySpec

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        data = {
            "Samsung S25 Ultra": [
                "Camera: 200MP Samsung HP3 sensor",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Samsung S25 FE": [
                "Camera: 50MP Sony IMX766",
                "Battery: 4500 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Samsung S24 Plus": [
                "Camera: 50MP GN3 sensor",
                "Battery: 4900 mAh",
                "Refresh Rate: 120Hz"
            ],

            "iPhone 17 Pro Max": [
                "Camera: 48MP Sony Quad-Pixel",
                "Battery: 4500 mAh",
                "Refresh Rate: 120Hz"
            ],
            "iPhone 17": [
                "Camera: 48MP Sony",
                "Battery: 3800 mAh",
                "Refresh Rate: 60Hz"
            ],
            "iPhone Air": [
                "Camera: 48MP Sony IMX703",
                "Battery: 4200 mAh",
                "Refresh Rate: 120Hz"
            ],

            "Huawei Mate 60": [
                "Camera: 50MP Sony IMX766",
                "Battery: 4750 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Huawei Mate X": [
                "Camera: 50MP Sony IMX766",
                "Battery: 4600 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Huawei Pura 70": [
                "Camera: 50MP OmniVision OV50H",
                "Battery: 5200 mAh",
                "Refresh Rate: 120Hz"
            ],

            "iQOO 13": [
                "Camera: 50MP Samsung GN5",
                "Battery: 5000 mAh",
                "Refresh Rate: 144Hz"
            ],
            "iQOO 15": [
                "Camera: 50MP GN5",
                "Battery: 5100 mAh",
                "Refresh Rate: 120Hz"
            ],
            "iQOO Neo 10 Pro": [
                "Camera: 50MP Sony IMX920",
                "Battery: 5500 mAh",
                "Refresh Rate: 120Hz"
            ],

            "Realme 15 Pro": [
                "Camera: 50MP Sony LYT600",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Realme GT 7 Pro": [
                "Camera: 50MP Sony IMX890",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Realme GT 8 Pro": [
                "Camera: 50MP Sony IMX966",
                "Battery: 5500 mAh",
                "Refresh Rate: 120Hz"
            ],

            "Vivo V60": [
                "Camera: 50MP Sony LYT600",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Vivo X Fold-3": [
                "Camera: 50MP Sony IMX866",
                "Battery: 5500 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Vivo X300 Pro": [
                "Camera: 50MP Sony IMX989",
                "Battery: 5500 mAh",
                "Refresh Rate: 120Hz"
            ],

            "Redmi Note 14 Pro": [
                "Camera: 200MP Samsung HP3",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Xiaomi 14": [
                "Camera: 50MP Leica Summilux",
                "Battery: 4610 mAh",
                "Refresh Rate: 120Hz"
            ],
            "Xiaomi 14 Civi": [
                "Camera: 50MP Sony LYT800",
                "Battery: 4700 mAh",
                "Refresh Rate: 120Hz"
            ],

            "OnePlus Nord 5": [
                "Camera: 50MP Sony IMX890",
                "Battery: 5000 mAh",
                "Refresh Rate: 120Hz"
            ],
            "OnePlus 13": [
                "Camera: 50MP + 48MP + 50MP",
                "Battery: 5500 mAh",
                "Refresh Rate: 120Hz"
            ],
            "OnePlus 15": [
                "Camera: 50MP triple",
                "Battery: 5800 mAh",
                "Refresh Rate: 120Hz"
            ],
        }

        for phone_name, specs in data.items():
            try:
                phone = Phone.objects.get(name__iexact=phone_name)
            except Phone.DoesNotExist:
                print("NOT FOUND:", phone_name)
                continue
            
            for line in specs:
                KeySpec.objects.create(phone=phone, text=line)

        self.stdout.write(self.style.SUCCESS("Key specs populated successfully!"))

