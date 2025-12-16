from django.core.management.base import BaseCommand
from homeappliances.models import HomeAppliances, HomeAppliancesKeyspecs

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        data = {
            "BlueStar 3 Ton Inverter AC": [
                "Refrigerant: R32 Eco-friendly",
                "Air Filter: Anti-microbial + Dust filter",
                "Compressor: Brushless DC Inverter"
            ],
            "Voltas 1.5 Ton Split AC": [
                "Refrigerant: R410A",
                "Air Filter: Anti-bacterial filter",
                "Special Modes: Turbo, Sleep Mode"
            ],
            "Wirpool 2 Ton Window AC": [
                "Refrigerant: R22",
                "Airflow: 450 CFM",
                "Compressor: Rotary Compressor"
            ],
            "LG 655 L Frost Free Side-by-Side": [
                "Compressor: Smart Inverter",
                "Special Feature: Door-in-Door + InstaView",
                "Deodorizer: Built-in Odor Control"
            ],
            "Samsung 396 L Frost Free Double Door" : [
                "Compressor: Digital Inverter",
                "Energy Rating: 3-Star",
                "Special Feature: Power Freeze / Power Cool"
            ],
            "Whirpool 240L Frost Free Double Door" : [
                "Compressor: 6th Sense Inverter",
                "Freshness: Honey-comb Moisture Lock",
                "Energy Rating: 2-Star"
            ],
            "Bosch 9kg Fully Automatic Front Load": [
                "Spin Speed: 1400 RPM",
                "Wash Programs: 15+ Programs",
                "Special Feature: Anti-Vibration Design"
            ],
            "LG Front Load 7kg": [
                "Spin Speed: 1200 RPM",
                "Wash Programs: 10+",
                "Feature: 6-Motion DD Wash"
            ],
            "Samsung 8kg 5 Star Inverter" : [
                "Spin Speed: 1400 RPM",
                "Wash Programs: 12",
                "Feature: EcoBubble Technology"
            ],
            "LG 55 inch 4K UHD Smart OLED TV" : [
                "HDR: Dolby Vision",
                "Sound: Dolby Atmos",
                "Refresh Rate: 120Hz"
            ],
            "Samsung 65 inch QLED 4K Smart TV" : [
                "HDR: Quantum HDR 32X",
                "Sound: Object Tracking Sound",
                "Processor: Quantum Processor 4K"
            ],
            "Sony Bravia 8 II 4K UHD Smart TV" : [
                "HDR: Dolby Vision + HDR10",
                "Sound: Acoustic Surface Audio+",
                "Processor: Cognitive Processor XR"
            ]
        }

        for homeappliances_name, specs in data.items():

            try:
                homeappliances = HomeAppliances.objects.get(name=homeappliances_name)

            except HomeAppliances.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"HomeAppliances not found: {homeappliances_name}"))
                continue

            for text in specs:
                HomeAppliancesKeyspecs.objects.create(homeappliances=homeappliances, text=text)

        self.stdout.write(self.style.SUCCESS("HomeAppliances Keyspecs populated successfully!"))