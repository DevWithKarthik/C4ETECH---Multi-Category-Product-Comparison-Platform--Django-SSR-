from django.core.management.base import BaseCommand
from tablets.models import Tablet, TabletKeyspecs

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        data = {
            "iPad Air" : [
                "Battery: 28.6 Wh",
                "Camera: 12MP Wide (f/1.8)",
                "Refresh Rate: 60Hz"
            ],
            "iPad Mini" : [
                "Battery: 19.3 Wh",
                "Camera: 12MP Wide",
                "Refresh Rate: 60Hz"
            ],
            "iPad Pro" : [
                "Battery: 31–38 Wh",
                "Camera: 12MP Wide (LiDAR)",
                "Refresh Rate: 120Hz ProMotion"
            ],
            "Lenovo IdeaTab Pro" : [
                "Battery: 8600 mAh",
                "Camera: 13MP rear",
                "Refresh Rate: 120Hz"
            ],
            "Lenovo Yoga Tab Plus" : [
                "Battery: 10200 mAh",
                "Camera: 13MP",
                "Refresh Rate: 120Hz"
            ],
            "Lenovo Tab Plus" : [
                "Battery: 8600 mAh",
                "Camera: 13MP",
                "Refresh Rate: 90Hz"
            ],
            "Samsung Galaxy Tab S9 FE+" : [
                "Battery: 10,090 mAh",
                "Camera: Dual 8MP",
                "Refresh Rate: 90Hz"
            ],
            "Samsung Galaxy Tab S10 FE" : [
                "Battery: 8840 mAh",
                "Camera: 12MP",
                "Refresh Rate: 90Hz"
            ],
            "Samsung Galaxy Tab S11" : [
                "Battery: 10,090 mAh",
                "Camera: 13MP",
                "Refresh Rate: 120Hz"
            ],
            "Redmi Pad Pro 5G" : [
                "Battery: 10,000 mAh",
                "Camera: 8MP",
                "Refresh Rate: 120Hz"
            ],
            "Xiaomi Pad 6" : [
                "Battery: 8840 mAh",
                "Camera: 13MP",
                "Refresh Rate: 144Hz"
            ],
            "Xiaomi Pad 7" : [
                "Battery: 10,000 mAh",
                "Camera: 50MP Sony",
                "Refresh Rate: 144Hz"
            ]
        }

        for tablet_name, specs in data.items():

            try:
                tablet = Tablet.objects.get(name=tablet_name)

            except Tablet.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Tablet not found: {tablet_name}"))
                continue

            for text in specs:
                TabletKeyspecs.objects.create(tablet=tablet, text=text)

        self.stdout.write(self.style.SUCCESS("Tablet Keyspecs populated successfully!"))