from django.contrib import admin
from django.utils.html import format_html
from .models import BrandHomeAppliances, HomeAppliances, HomeAppliancesOverview, HomeAppliancesKeyspecs

# Register your models here.

class HomeAppliancesOverviewInline(admin.TabularInline):
    model = HomeAppliancesOverview
    extra = 1

class HomeAppliancesKeyspecsInline(admin.TabularInline):
    model = HomeAppliancesKeyspecs
    extra=1

class HomeAppliancesAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")

    inlines = [HomeAppliancesKeyspecsInline, HomeAppliancesOverviewInline]


class BrandHomeApplianceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


admin.site.register(BrandHomeAppliances, BrandHomeApplianceAdmin)
admin.site.register(HomeAppliances, HomeAppliancesAdmin)