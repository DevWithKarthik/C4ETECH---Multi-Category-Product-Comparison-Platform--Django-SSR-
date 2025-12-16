from django.core.management.base import BaseCommand
from laptops.models import Laptop, LaptopKeyspecs

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        data = {
            "Dell Alienware 16 Area": [
                "GPU: NVIDIA RTX 4070",
                "Battery: 90Wh",
                "Graphics Card: GeForce RTX 40-Series"
            ],
            "Dell Inspiron 14 Plus": [
                "GPU: Intel Iris Xe",
                "Battery: 65Wh",
                "Graphics Card: Integrated graphics"
            ],
            "Dell 16 Premium": [
                "GPU: NVIDIA RTX 4050 / 4060",
                "Battery: 86Wh",
                "Graphics Card: RTX 40-Series"
            ],
            "ASUS ProArt P16": [
                "GPU: NVIDIA RTX 4060",
                "Battery: 96Wh",
                "Graphics Card: NVIDIA GeForce RTX Series"
            ],
            "ASUS ROG Zephyrus G16": [
                "GPU: NVIDIA RTX 4070",
                "Battery: 90Wh",
                "Graphics Card: GeForce RTX 40-Series"
            ],
            "ASUS Zenbook 14 OLED": [
                "GPU: Integrated Intel Iris Xe",
                "Battery: 75Wh",
                "Graphics Card: Integrated Xe Graphics"
            ],
            "HP OmniBook 7 Aero": [
                "GPU: Intel Arc Integrated",
                "Battery: 68Wh",
                "Graphics Card: Intel Arc"
            ],
            "HP OmniBook X Flip 14": [
                "GPU: Qualcomm Adreno GPU",
                "Battery: 70Wh",
                "Graphics Card: Integrated Adreno"
            ],
            "HP Omen 16": [
                "GPU: NVIDIA RTX 4060",
                "Battery: 83Wh",
                "Graphics Card: GeForce RTX 40-Series"
            ],
            "Lenovo Legion Pro 7i": [
                "GPU: NVIDIA RTX 4080",
                "Battery: 99Wh",
                "Graphics Card: GeForce RTX 40-Series"
            ],
            "Lenovo ThinkPad X1 Carbon": [
                "GPU: Intel Iris Xe",
                "Battery: 57Wh",
                "Graphics Card: Integrated Xe"
            ],
            "Lenovo Yoga Slim 7": [
                "GPU: Radeon 780M",
                "Battery: 67Wh",
                "Graphics Card: Radeon Integrated"
            ],
            "MacBook Air 13 (M3)": [
                "GPU: Apple 10-core GPU",
                "Battery: 52.6Wh",
                "Graphics Card: Integrated (M3 GPU)"
            ],
            "MacBook Pro 16": [
                "GPU: 18-core or 30-core GPU",
                "Battery: 100Wh",
                "Graphics Card: M3 Pro/Max integrated GPU"
            ],
            "MacBook Pro 14": [
                "GPU: 14 / 30 core GPU",
                "Battery: 70Wh",
                "Graphics Card: Apple GPU"
            ],
            "Acer Nitro 16": [
                "GPU: NVIDIA RTX 4060",
                "Battery: 90Wh",
                "Graphics Card: GeForce RTX"
            ],
            "Acer Swift Go 14": [
                "GPU: Intel Arc",
                "Battery: 65Wh",
                "Graphics Card: Integrated Arc"
            ],
            "Acer ConceptD 7 Ezel": [
                "GPU: NVIDIA RTX 3080",
                "Battery: 75Wh",
                "Graphics Card: GeForce RTX"
            ],
        }

        for laptop_name, specs in data.items():

            try:
                laptop = Laptop.objects.get(name=laptop_name)

            except Laptop.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Laptop not found: {laptop_name}"))
                continue

            for text in specs:
                LaptopKeyspecs.objects.create(laptop=laptop, text=text)

        self.stdout.write(self.style.SUCCESS("Laptop Keyspecs populated successfully!"))
