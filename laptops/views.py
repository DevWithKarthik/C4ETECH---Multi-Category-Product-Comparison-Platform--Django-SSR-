from django.shortcuts import render, get_object_or_404
from .models import BrandLaptop, Laptop, LaptopOverview, LaptopKeyspecs

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

def laptops(request):
    brands = BrandLaptop.objects.all()
    return render(request, "laptops/laptops.html", {"brands" : brands})

def brand_details(request, brand):
    
    brand_obj = get_object_or_404(BrandLaptop, slug=brand)

    laptops = Laptop.objects.filter(brand=brand_obj).prefetch_related("overviews", "keyspecs")
    
    return render(request, "laptops/laptop_details.html",{"brand": brand_obj, "laptops": laptops,},)

