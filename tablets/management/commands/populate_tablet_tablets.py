from django.core.management.base import BaseCommand
from tablets.models import BrandTablets, Tablet

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        laptops = {
            "ipad" : [
                ("iPad Air", "tablets/ipad/iPad-Air.webp"),
                ("iPad Mini", "tablets/ipad/iPad-mini.webp"),
                ("iPad Pro", "tablets/ipad/iPad-pro.webp")
            ],
            "lenovo" : [
                ("Lenovo IdeaTab Pro", "tablets/lenovo/Lenovo-Idea-Tab-Pro.webp"),
                ("Lenovo Yoga Tab Plus", "tablets/lenovo/Lenovo-Yoga-Tab-Plus.webp"),
                ("Lenovo Tab Plus", "tablets/lenovo/Lenovo-tab-plus.webp")
            ],
            "samsung" : [
                ("Samsung Galaxy Tab S9 FE+", "tablets/Samsung/Galaxy-S9-FE+.webp"),
                ("Samsung Galaxy Tab S10 FE", "tablets/Samsung/Galaxy-S10-FE.webp"),
                ("Samsung Galaxy Tab S11", "tablets/Samsung/Galaxy-S11-tab.webp")
            ],
            "xiaomi" : [
                ("Redmi Pad Pro 5G", "tablets/Xiaomi/Redmi-Pad-Pro-5g.webp"),
                ("Xiaomi Pad 6", "tablets/Xiaomi/Redmi-Pad-6.webp"),
                ("Xiaomi Pad 7", "tablets/Xiaomi/Xiaomi-Pad-7.jpg")
            ]
        }

        for slug, laptop_list in laptops.items():
            brand = BrandTablets.objects.get(slug=slug)

            for name, img in laptop_list:
                Tablet.objects.get_or_create(
                    brand = brand,
                    name = name,
                    defaults={"image" : img}
                )

        self.stdout.write(self.style.SUCCESS("Laptops populated successfully!"))