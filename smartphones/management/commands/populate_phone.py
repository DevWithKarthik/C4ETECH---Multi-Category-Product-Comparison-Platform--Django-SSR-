from django.core.management.base import BaseCommand
from smartphones.models import Brand, Phone

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        phones = {
            "samsung": [
                ("Samsung S25 Ultra", "smartphones/samsung/S25-Ultra1.webp"),
                ("Samsung S25 FE", "smartphones/samsung/S25-FE.avif"),
                ("Samsung S24 Plus", "smartphones/samsung/S24-plus.jpg"),
            ],

            "apple": [
                ("iPhone 17 Pro Max", "smartphones/apple/17-pro-max.webp"),
                ("iPhone 17", "smartphones/Apple/Apple_17.png"),
                ("iPhone Air", "smartphones/apple/Apple-iPhone-Air.webp"),
            ],

            "huawei": [
                ("Huawei Mate 60", "smartphones/huawei/Huawei-mate-60.jpg"),
                ("Huawei Mate X", "smartphones/huawei/Huawei-mate-X.avif"),
                ("Huawei Pura 70", "smartphones/huawei/pura-70.png"),
            ],

            "iqoo": [
                ("iQOO 13", "smartphones/iQOO/iqoo-13.png"),
                ("iQOO 15", "smartphones/iQOO/iqoo-15.png"),
                ("iQOO Neo 10 Pro", "smartphones/iQOO/iqoo-neo10-pro.png"),
            ],

            "oneplus": [
                ("OnePlus Nord 5", "smartphones/oneplus/NORD-5.webp"),
                ("OnePlus 13", "smartphones/oneplus/oneplus-13.png"),
                ("OnePlus 15", "smartphones/oneplus/oneplus-15.jpg"),
            ],

            "realme": [
                ("Realme 15 Pro", "smartphones/realme/realme-15pro.png"),
                ("Realme GT 7 Pro", "smartphones/realme/realme-GT-7pro.webp"),
                ("Realme GT 8 Pro", "smartphones/realme/realme-gt-8pro.webp"),
            ],

            "vivo": [
                
                ("Vivo V60", "smartphones/Vivo/Vivo-V60.webp"),
                ("Vivo X Fold-3", "smartphones/Vivo/Vivo-X-Fold3.jpg"),
                ("Vivo X300 Pro", "smartphones/Vivo/X300pro.jpg"),
            ],

            "xiaomi": [
                ("Redmi Note 14 Pro", "smartphones/Xiaomi/Redmi-note-14-Pro.png"),
                ("Xiaomi 14", "smartphones/Xiaomi/Xiaomi-14.png"),
                ("Xiaomi 14 Civi", "smartphones/Xiaomi/Xiaomi-14-civi.png"),
            ],
        }

        for slug, phone_list in phones.items():
            brand = Brand.objects.get(slug=slug)
            for name, img in phone_list:
                Phone.objects.get_or_create(
                    brand=brand,
                    name=name,
                    defaults={"image": img}
                )

        self.stdout.write(self.style.SUCCESS("Phones populated successfully!"))
