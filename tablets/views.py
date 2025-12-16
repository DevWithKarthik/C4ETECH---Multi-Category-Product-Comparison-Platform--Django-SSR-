from django.shortcuts import render, get_object_or_404
from .models import BrandTablets, Tablet, TabletKeyspecs, TabletOverview

# Create your views here.

# tablets_brands_data = {
#     "samsung": {
#         "title": "Samsung",
#         "img" : "smartphones/samsung.png",
#         "models": [
#             {
#                 "name": "Samsung Tab - S10",
#                 "img": "smartphones/samsung/S25-Ultra1.webp",
#                 "overview": [
#                     "Display: 6.8 AMOLED",
#                     "Chipset: Snapdragon / Exynos",
#                     "RAM: 12GB"
#                 ],
#                 "key_specs": [
#                     "Battery: 5000 mAh",
#                     "Camera: 200 MP",
#                     "OS: Android 15",
#                 ]
#             },
#             {
#                 "name": "Samsung - Tab S9",
#                 "img": "smartphones/samsung/S25-FE.avif",
#                 "overview": [
#                     "Display: 6.5 AMOLED",
#                     "Chipset: Mid-range",
#                     "RAM: 8GB"
#                 ],
#                 "key_specs": [
#                     "Battery: 4500 mAh",
#                     "Camera: 64 MP",
#                     "Price Tier: Mid",
#                 ]
#             }
#         ]
#     },
#     "lenovo" : {
#         "title" : "LENOVO",
#         "img" : "smartphones/apple.png",
#         "models": [
#             {
#                 "name": "Lenovo - 1",
#                 "img": "smartphones/samsung/S25-Ultra1.webp",
#                 "overview": [
#                     "Display: 6.8 AMOLED",
#                     "Chipset: Snapdragon / Exynos",
#                     "RAM: 12GB"
#                 ],
#                 "key_specs": [
#                     "Battery: 5000 mAh",
#                     "Camera: 200 MP",
#                     "OS: Android 15",
#                 ]
#             },
#             {
#                 "name": "Lenovo - 2",
#                 "img": "smartphones/samsung/S25-FE.avif",
#                 "overview": [
#                     "Display: 6.5 AMOLED",
#                     "Chipset: Mid-range",
#                     "RAM: 8GB"
#                 ],
#                 "key_specs": [
#                     "Battery: 4500 mAh",
#                     "Camera: 64 MP",
#                     "Price Tier: Mid",
#                 ]
#             }
#         ]
#     }
# }


def tablets(request):
    brands = BrandTablets.objects.all()
    return render(request, "tablets/tablets.html", {"brands" : brands})


def brand_details(request, brand):
    
    brand_obj = get_object_or_404(BrandTablets, slug=brand)

    tablets = Tablet.objects.filter(brand=brand_obj).prefetch_related("overviews", "keyspecs")
    
    return render(request, "tablets/tablet_details.html",{"brand": brand_obj, "tablets": tablets,},)


