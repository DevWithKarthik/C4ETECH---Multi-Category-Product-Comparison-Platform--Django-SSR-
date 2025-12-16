from django.contrib import admin
from django.utils.html import format_html
from .models import BrandLaptop, Laptop, LaptopOverview, LaptopKeyspecs

# Register your models here.

class LaptopOverviewInline(admin.TabularInline):
    model = LaptopOverview
    extra = 1

class LaptopKeyspecsInline(admin.TabularInline):
    model = LaptopKeyspecs
    extra=1

class LaptopAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")

    inlines = [LaptopKeyspecsInline, LaptopOverviewInline]


class LaptopBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


admin.site.register(BrandLaptop, LaptopBrandAdmin)
admin.site.register(Laptop, LaptopAdmin)