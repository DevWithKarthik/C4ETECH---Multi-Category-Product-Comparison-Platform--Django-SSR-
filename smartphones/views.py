from django.shortcuts import render, get_object_or_404
from smartphones.models import Brand, Phone, Overview, KeySpec

# Create your views here.

# brand = [
#     {
#         "name" : "Samsung",
#         "img" : "smartphones/samsung.png",
#     },
#     {
#         "name" : "Apple",
#         "img" : "smartphones/apple.png",
#     },
#     {
#         "name" : "Huawei",
#         "img" : "smartphones/Huawei-Logo.png",
#     },
#     {
#         "name" : "iQOO",
#         "img" : "smartphones/iQOO.jpg",
#     },
#     {
#         "name" : "Vivo",
#         "img" : "smartphones/vivo.webp",
#     },
#     {
#         "name" : "Realme",
#         "img" : "smartphones/realme-logo.png",
#     },
#     {
#         "name" : "Xiaomi",
#         "img" : "smartphones/Xiaomi-logo.png",
#     },
#     {
#         "name" : "Oneplus",
#         "img" : "smartphones/oneplus.png",
#     },
# ]

# brands_data = {
#     "samsung": {
#         "title": "Samsung",
#         "img" : "smartphones/samsung.png",
#         "models": [
#             {
#                 "name": "Samsung S25 Ultra",
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
#                 "name": "Samsung S25 FE",
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
#     "apple" : {
#         "title" : "Apple",
#         "img" : "smartphones/apple.png",
#         "models": [
#             {
#                 "name": "Apple 17 Pro Max",
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
#                 "name": "Apple 17 AIR",
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

from django.shortcuts import render, get_object_or_404
from .models import Brand, Phone, Overview, KeySpec

def smartphone(request):
    brands = Brand.objects.all()
    return render(request, "smartphones/smartphone.html", {"brands": brands})

def brand_details(request, brand):
    brand_obj = get_object_or_404(Brand, slug=brand)

    phones = Phone.objects.filter(brand=brand_obj).prefetch_related("overview_set", "keyspec_set")

    return render(request, "smartphones/brand_details.html", {
        "brand": brand_obj,
        "phones": phones,
    })
