from django.core.management.base import BaseCommand
from tablets.models import Tablet, TabletOverview

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        data = {
            "iPad Air" : [
                "Display: 10.9″ Liquid Retina",
                "Chipset: Apple M2",
                "RAM / Storage: 8GB / 128GB, 512GB"
            ],
            "iPad Mini" : [
                "Display: 8.3″ Liquid Retina"
                "Chipset: Apple A17 (Next-Gen Mini)",
                "RAM / Storage: 6GB / 64GB, 256GB"
            ],
            "iPad Pro" : [
                "Display: 11″ / 13″ Ultra Retina (OLED)",
                "Chipset: Apple M4",
                "RAM / Storage: 8GB, 16GB / 256GB, 2TB"
            ],
            "Lenovo IdeaTab Pro" : [
                "Display: 11.5″ 2K OLED",
                "Chipset: Snapdragon 870",
                "RAM / Storage: 6GB, 8GB / 128GB, 256GB"
            ],
            "Lenovo Yoga Tab Plus" : [
                "Display: 11.5″ 2.8K",
                "Chipset: Snapdragon 8 Gen 1",
                "RAM / Storage: 8GB / 128GB, 256GB"
            ],
            "Lenovo Tab Plus" : [
                "Display: 11.5″ IPS",
                "Chipset: MediaTek Dimensity 7050",
                "RAM / Storage: 8GB / 128GB, 256GB"
            ],
            "Samsung Galaxy Tab S9 FE+" : [
                "Display: 12.4″ LCD",
                "Chipset: Exynos 1380",
                "RAM / Storage: 8GB, 12GB / 128GB, 256GB"
            ],
            "Samsung Galaxy Tab S10 FE" : [
                "Display: 11″ LCD",
                "Chipset: Exynos 1480",
                "RAM / Storage: 8GB / 128GB, 256GB"
            ],
            "Samsung Galaxy Tab S11" : [
                "Display: 11.4″ AMOLED",
                "Chipset: Snapdragon 8 Gen 3",
                "RAM / Storage: 12GB / 256GB, 512GB"
            ],
            "Redmi Pad Pro 5G" : [
                "Display: 12.1″ 2.5K",
                "Chipset: MediaTek Dimensity 9200+",
                "RAM / Storage: 6GB, 8GB / 128GB, 256GB"
            ],
            "Xiaomi Pad 6" : [
                "Display: 11″ 2.5K",
                "Chipset: Snapdragon 870",
                "RAM / Storage: 6GB, 8GB / 128GB, 256GB"
            ],
            "Xiaomi Pad 7" : [
                "Display: 11″ AMOLED",
                "Chipset: Snapdragon 8 Gen 2",
                "RAM / Storage: 8GB, 12GB / 256GB, 512GB"
            ]
        }

        for tablet_name, specs in data.items():
            try:
                tablet = Tablet.objects.get(name=tablet_name)
            except Tablet.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Tablet not found: {tablet_name}"))
                continue

            for line in specs:
                TabletOverview.objects.create(tablet=tablet, text=line)
        self.stdout.write(self.style.SUCCESS("Tablet Overview populated successfully!"))