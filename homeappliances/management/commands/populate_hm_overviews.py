from django.core.management.base import BaseCommand
from homeappliances.models import HomeAppliances, HomeAppliancesOverview

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        data = {
            "BlueStar 3 Ton Inverter AC": [
                "Capacity: 3 Ton",
                "Type: Inverter Split AC",
                "Energy Rating: 5 Star"
            ],
            "Voltas 1.5 Ton Split AC": [
                "Capacity: 1.5 Ton",
                "Type: Split AC",
                "Energy Rating: 3 Star"
            ],
            "Wirpool 2 Ton Window AC": [
                "Capacity: 2 Ton",
                "Type: Window AC",
                "Energy Rating: 4 Star"
            ],
            "LG 655 L Frost Free Side-by-Side": [
                "Capacity: 655 Liters",
                "Type: Frost Free Side-by-Side",
                "Energy Rating: 4 Star"
            ],
            "Samsung 396 L Frost Free Double Door": [
                "Capacity: 396 Liters",
                "Type: Frost Free Double Door",
                "Energy Rating: 3 Star"
            ],
            "Whirpool 240L Frost Free Double Door": [
                "Capacity: 240 Liters",
                "Type: Frost Free Double Door",
                "Energy Rating: 3 Star"
            ],
            "Bosch 9kg Fully Automatic Front Load": [
                "Capacity: 9 kg",
                "Type: Fully Automatic Front Load",
                "Spin Speed: 1400 RPM"
            ],
            "LG Front Load 7kg": [
                "Capacity: 7 kg",
                "Type: Front Load",
                "Spin Speed: 1200 RPM"
            ],
            "Samsung 8kg 5 Star Inverter": [
                "Capacity: 8 kg",
                "Type: Inverter Fully Automatic",
                "Spin Speed: 1400 RPM"
            ],
            "LG 55 inch 4K UHD Smart OLED TV": [
                "Screen Size: 55 inches",
                "Resolution: 4K UHD",
                "Type: Smart OLED"
            ],
            "Samsung 65 inch QLED 4K Smart TV": [
                "Screen Size: 65 inches",
                "Resolution: 4K UHD",
                "Type: QLED Smart"
            ],
            "Sony Bravia 8 II 4K UHD Smart TV": [
                "Screen Size: 55 inches",
                "Resolution: 4K UHD",
                "Type: Smart LED"
            ]
        }

        for homeappliances_name, specs in data.items():
            try:
                homeappliances = HomeAppliances.objects.get(name=homeappliances_name)
            except HomeAppliances.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Home Appliances not found: {homeappliances_name}"))
                continue

            for line in specs:
                HomeAppliancesOverview.objects.create(homeappliances=homeappliances, text=line)
        self.stdout.write(self.style.SUCCESS("Home Appliances Overview populated successfully!"))