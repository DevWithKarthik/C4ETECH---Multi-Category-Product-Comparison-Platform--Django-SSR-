from django.core.management.base import BaseCommand
from homeappliances.models import BrandHomeAppliances, HomeAppliances

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        homeappliances = {
            "air-conditioner" : [
                ("BlueStar 3 Ton Inverter AC", "homeappliances/AC/3-ton-blue-star.jpg"),
                ("Voltas 1.5 Ton Split AC", "homeappliances/AC/Voltas_ac.webp"),
                ("Wirpool 2 Ton Window AC", "homeappliances/AC/Wirpool.avif")
            ],
            "refrigerator" : [
                ("LG 655 L Frost Free Side-by-Side", "homeappliances/fridge/LG-655-L.webp"),
                ("Samsung 396 L Frost Free Double Door", "homeappliances/fridge/Samsung-396-L.webp"),
                ("Whirpool 240L Frost Free Double Door", "homeappliances/fridge/Whirpool-240L.webp")
            ],

            "washing-machine" : [
                ("Bosch 9kg Fully Automatic Front Load", "homeappliances/washing_machine/Bosch-9kg-Fully-Automatic.webp"),
                ("LG Front Load 7kg", "homeappliances/washing_machine/LG-Front-Load.webp"),
                ("Samsung 8kg 5 Star Inverter", "homeappliances/washing_machine/Samsung-8kg-5-Star-Inverter.webp")
            ],
            "television" : [
                ("LG 55 inch 4K UHD Smart OLED TV", "homeappliances/TV/LG-4K-Ultra-HD.webp"),
                ("Samsung 65 inch QLED 4K Smart TV", "homeappliances/TV/Samsung-OLED-4K.webp"),
                ("Sony Bravia 8 II 4K UHD Smart TV", "homeappliances/TV/Sony-Bravia-8-II-4K.webp")
            ]
        }

        for slug, homeapp_list in homeappliances.items():
            brand = BrandHomeAppliances.objects.get(slug=slug)

            for name, img in homeapp_list:
                HomeAppliances.objects.get_or_create(
                    brand = brand,
                    name = name,
                    defaults={"image" : img}
                )

        self.stdout.write(self.style.SUCCESS("Home Appliances populated successfully!"))