from django.shortcuts import render

# Create your views here.



data = [
    {"product": "SMARTPHONES", "url": "smartphones:home"},
    {"product": "LAPTOPS", "url": "laptops:home"},
    {"product": "TABLETS", "url": "tablets:home"},
    {"product": "HOME APPLIANCES", "url": "homeappliances:home"},
]

def index(request):
    return render(request, "c4etech/index.html", {"data": data})

