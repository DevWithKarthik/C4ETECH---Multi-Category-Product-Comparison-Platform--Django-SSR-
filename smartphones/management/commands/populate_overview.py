from django.core.management.base import BaseCommand
from smartphones.models import Phone, Overview

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        data = {
            "Samsung S25 Ultra": [
                "Display: 6.8 AMOLED",
                "Chipset: Snapdragon 8 Elite",
                "RAM / Storage: 12GB / 256GB"
            ],
            "Samsung S25 FE": [
                "Display: 6.5 AMOLED",
                "Chipset: Mid-range Snapdragon",
                "RAM / Storage: 8GB / 128GB"
            ],
            "Samsung S24 Plus": [
                "Display: 6.7 AMOLED",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 8GB / 256GB"
            ],

            "iPhone 17 Pro Max": [
                "Display: 6.9 LTPO OLED",
                "Chipset: A19 Bionic",
                "RAM / Storage: 8GB / 256GB"
            ],
            "iPhone 17": [
                "Display: 6.1 OLED",
                "Chipset: A19",
                "RAM / Storage: 6GB / 128GB"
            ],
            "iPhone Air": [
                "Display: 6.5 OLED",
                "Chipset: A18",
                "RAM / Storage: 6GB / 128GB"
            ],

            "Huawei Mate 60": [
                "Display: 6.69 LTPO OLED, 120Hz",
                "Chipset: Kirin 9000S",
                "RAM / Storage: 12GB / 256-512GB"
            ],
            "Huawei Mate X": [
                "Display: 7.8 Foldable OLED, 120Hz",
                "Chipset: Kirin 9000 series",
                "RAM / Storage: 12GB / 512GB"
            ],
            "Huawei Pura 70": [
                "Display: 6.76 OLED, 120Hz",
                "Chipset: Kirin 9010",
                "RAM / Storage: 12GB / 256GB"
            ],

            "iQOO 13": [
                "Display: 6.78 AMOLED, 144Hz",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 256GB"
            ],
            "iQOO 15": [
                "Display: 6.78 AMOLED",
                "Chipset: Snapdragon 8 Gen 4",
                "RAM / Storage: 12GB / 256GB"
            ],
            "iQOO Neo 10 Pro": [
                "Display: 6.78 AMOLED, 120Hz",
                "Chipset: Snapdragon 8s Gen 3",
                "RAM / Storage: 12GB / 256GB"
            ],

            "Realme 15 Pro": [
                "Display: 6.7 AMOLED, 120Hz",
                "Chipset: Snapdragon 7s Gen 2",
                "RAM / Storage: 8GB / 128GB"
            ],
            "Realme GT 7 Pro": [
                "Display: 6.78 AMOLED",
                "Chipset: Snapdragon 8 Gen 4",
                "RAM / Storage: 12GB / 256GB"
            ],
            "Realme GT 8 Pro": [
                "Display: 6.7 AMOLED, 1220p",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 256GB"
            ],

            "Vivo V60": [
                "Display: 6.7 AMOLED",
                "Chipset: Dimensity 8300",
                "RAM / Storage: 12GB / 256GB"
            ],
            "Vivo X Fold-3": [
                "Display: 7.85 foldable AMOLED",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 512GB"
            ],
            "Vivo X300 Pro": [
                "Display: 6.78 AMOLED",
                "Chipset: Snapdragon 8 Gen 4",
                "RAM / Storage: 16GB / 1TB"
            ],

            "Redmi Note 14 Pro": [
                "Display: 6.7 AMOLED, 120Hz",
                "Chipset: Snapdragon 7s Gen 2",
                "RAM / Storage: 8GB / 256GB"
            ],
            "Xiaomi 14": [
                "Display: 6.36 AMOLED, 120Hz",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 512GB"
            ],
            "Xiaomi 14 Civi": [
                "Display: 6.55 AMOLED",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 256GB"
            ],

            "OnePlus NORD 5": [
                "Display: 6.74 AMOLED, 120Hz",
                "Chipset: Snapdragon 7+ Gen 2",
                "RAM / Storage: 8GB / 128GB"
            ],
            "OnePlus 13": [
                "Display: 6.8 LTPO AMOLED",
                "Chipset: Snapdragon 8 Gen 4",
                "RAM / Storage: 12GB / 256GB"
            ],
            "OnePlus 15": [
                "Display: 6.8 AMOLED, 120Hz",
                "Chipset: Snapdragon 8 Gen 5",
                "RAM / Storage: 12GB / 512GB"
            ],
        }

        for phone_name, specs in data.items():
            try:
                phone = Phone.objects.get(name=phone_name)
            except Phone.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Phone not found: {phone_name}"))
                continue

            for line in specs:
                Overview.objects.create(phone=phone, text=line)

        self.stdout.write(self.style.SUCCESS("Overview populated successfully!"))


