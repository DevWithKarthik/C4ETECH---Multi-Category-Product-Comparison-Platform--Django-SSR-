from django.core.management.base import BaseCommand
from laptops.models import Laptop, LaptopOverview

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        data = {
            "Dell Alienware 16 Area": [
                "Display: 16″ QHD+ 240Hz",
                "Processor: Intel Core i9-14900HX",
                "RAM / Storage: 16GB, 32GB / 1TB SSD"
            ],
            "Dell Inspiron 14 Plus": [
                "Display: 14″ 2.2K IPS",
                "Processor: Intel Core i7-1360P",
                "RAM / Storage: 16GB / 512GB SSD"
            ],
            "Dell 16 Premium": [
                "Display: 16.3″ OLED 4K",
                "Processor: Intel Core Ultra 7 155H",
                "RAM / Storage: 16GB, 32GB / 1TB SSD"
            ],
            "ASUS ProArt P16": [
                "Display: 16″ 4K OLED, 100% DCI-P3",
                "Processor: Intel Core i9-13900H",
                "RAM / Storage: 16GB / 1TB SSD",
            ],
            "ASUS ROG Zephyrus G16": [
                "Display: 16″ QHD+ 240Hz ROG Nebula",
                "Processor: AMD Ryzen 9 7940HS",
                "RAM / Storage: 16GB / 512GB, 1TB SSD"
            ],
            "ASUS Zenbook 14 OLED": [
                "Display: 14″ 2.8K OLED, 90Hz",
                "Processor: Intel Core i7-1360P",
                "RAM / Storage: 16GB / 512GB SSD"
            ],
            "HP OmniBook 7 Aero": [
                "Display: 14″ OLED 120Hz",
                "Processor: Intel Core Ultra 7",
                "RAM / Storage: 16GB / 512GB"
            ],
            "HP OmniBook X Flip 14": [
                "Display: 14″ 2.8K OLED Touch",
                "Processor: Snapdragon X Elite",
                "RAM / Storage: 16GB / 1TB"
            ],
            "HP Omen 16": [
                "Display: 16″ QHD 165Hz",
                "Processor: Intel Core i7-13700HX",
                "RAM / Storage: 16GB / 1TB SSD"
            ],
            "Lenovo Legion Pro 7i": [
                "Display: 16″ QHD+ 240Hz",
                "Processor: Intel Core i9-14900HX",
                "RAM / Storage: 32GB / 1TB SSD"
            ],
            "Lenovo ThinkPad X1 Carbon": [
                "Display: 14″ 2.8K OLED",
                "Processor: Intel Core i7-1365U",
                "RAM / Storage: 16GB / 512GB"
            ],
            "Lenovo Yoga Slim 7": [
                "Display: 14″ 2.8K OLED",
                "Processor: AMD Ryzen 7 7840U",
                "RAM / Storage: 16GB / 512GB"
            ],
            "MacBook Air 13 (M3)": [
                "Display: 13.6″ Liquid Retina",
                "Processor: Apple M3",
                "RAM / Storage: 8GB / 256GB"
            ],
            "MacBook Pro 16": [
                "Display: 16.2″ Liquid Retina XDR",
                "Processor: Apple M3 Pro / M3 Max",
                "RAM / Storage: 18GB, 36GB / 512GB+"
            ],
            "MacBook Pro 14": [
                "Display: 14.2″ Liquid Retina XDR",
                "Processor: M3 Pro / M3 Max",
                "RAM / Storage: 18GB / 512GB"
            ],
            "Acer Nitro 16": [
                "Display: 16″ QHD 165Hz",
                "Processor: AMD Ryzen 7 7840HS",
                "RAM / Storage: 16GB / 512GB"
            ],
            "Acer Swift Go 14": [
                "Display: 14″ 2.8K OLED",
                "Processor: Intel Core Ultra 5",
                "RAM / Storage: 16GB / 512GB"
            ],
            "Acer ConceptD 7 Ezel": [
                "Display: 15.6″ 4K touchscreen",
                "Processor: Intel Core i7-11800H",
                "RAM / Storage: 32GB / 1TB"
            ]
        }

        for laptop_name, specs in data.items():
            try:
                laptop = Laptop.objects.get(name=laptop_name)
            except Laptop.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Laptop not found: {laptop_name}"))
                continue

            for line in specs:
                LaptopOverview.objects.create(laptop=laptop, text=line)

        self.stdout.write(self.style.SUCCESS("Laptop Overview populated successfully!"))
