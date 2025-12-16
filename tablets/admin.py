from django.contrib import admin
from django.utils.html import format_html
from .models import BrandTablets, Tablet, TabletOverview, TabletKeyspecs

# Register your models here.

class TabletOverviewInline(admin.TabularInline):
    model = TabletOverview
    extra = 1

class TabletKeyspecsInline(admin.TabularInline):
    model = TabletKeyspecs
    extra=1

class TabletAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")

    inlines = [TabletKeyspecsInline, TabletOverviewInline]


class BrandTabletsAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


admin.site.register(BrandTablets, BrandTabletsAdmin)
admin.site.register(Tablet, TabletAdmin)