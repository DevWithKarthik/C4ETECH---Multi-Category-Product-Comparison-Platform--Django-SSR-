from django.core.management.base import BaseCommand
from laptops.models import BrandLaptop, Laptop

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        laptops = {
            "dell" : [
                ("Dell Alienware 16 Area", "laptops/DELL/Alienware_16_Area.avif"),
                ("Dell Inspiron 14 Plus", "laptops/DELL/Dell-14-plus.avif"),
                ("Dell 16 Premium", "laptops/DELL/Dell-16-Premium.webp")
            ],
            "acer" : [
                ("Acer Nitro 16", "laptops/acer/Acer-Nitro-16.webp"),
                ("Acer Swift Go 14", "laptops/acer/acer-Swift-Go-14.webp"),
                ("Acer ConceptD 7 Ezel", "laptops/acer/ConceptD7-Ezel.jpg")
            ],
            "asus" : [
                ("ASUS ProArt P16", "laptops/Asus/asus-proArt-p16.webp"),
                ("ASUS ROG Zephyrus G16", "laptops/Asus/asus-ROG-Zephyrus-G16.png"),
                ("ASUS Zenbook 14 OLED", "laptops/Asus/asus-zenbook-14-oled.webp"),
            ],
            "hp" : [
                ("HP OmniBook 7 Aero", "laptops/HP/HP-omnibook_x_flip_14.avif"),
                ("HP OmniBook X Flip 14", "laptops/HP/HP-Omnibook-7-Aero.png"),
                ("HP Omen 16", "laptops/HP/HPPomen.avif"),
            ],
            "lenovo" : [
                ("Lenovo Legion Pro 7i", "laptops/Lenovo/Lenovo-legion-pro-7i.webp"),
                ("Lenovo ThinkPad X1 Carbon", "laptops/Lenovo/Lenovo-Thinkpad-X1.webp"),
                ("Lenovo Yoga Slim 7", "laptops/Lenovo/lenovo-yoga-slim.webp")
            ],
            "apple" : [
                ("MacBook Air 13 (M3)", "laptops/MAC/Apple-MacBook-Air-13.webp"),
                ("MacBook Pro 16", "laptops/MAC/MacBook-Pro-16.png"),
                ("MacBook Pro 14", "laptops/MAC/Macbook-pro-14.webp")
            ]
        }

        for slug, laptop_list in laptops.items():
            brand = BrandLaptop.objects.get(slug=slug)

            for name, img in laptop_list:
                Laptop.objects.get_or_create(
                    brand = brand,
                    name = name,
                    defaults={"image" : img}
                )

        self.stdout.write(self.style.SUCCESS("Laptops populated successfully!"))