from django.shortcuts import render, get_object_or_404
from .models import BrandHomeAppliances, HomeAppliances, HomeAppliancesKeyspecs, HomeAppliancesOverview

# Create your views here.

# laptops_brands_data = {
#     "dell": {
#         "title": "Dell",
#         "img" : "smartphones/samsung.png",
#         "models": [
#             {
#                 "name": "Dell - 1",
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
#                 "name": "Dell-2",
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
#     "hp" : {
#         "title" : "HP",
#         "img" : "smartphones/apple.png",
#         "models": [
#             {
#                 "name": "HP - 1",
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
#                 "name": "HP - 2",
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

def homeappliacnes(request):
    brands = BrandHomeAppliances.objects.all()
    return render(request, "homeappliances/homeappliances.html", {"brands" : brands})

def brand_details(request, brand):
    
    brand_obj = get_object_or_404(BrandHomeAppliances, slug=brand)

    homeappliacnes = HomeAppliances.objects.filter(brand=brand_obj).prefetch_related("overviews", "keyspecs")
    
    return render(request, "homeappliances/hm_details.html",{"brand": brand_obj, "homeappliances": homeappliacnes,},)

