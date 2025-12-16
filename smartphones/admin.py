from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Phone, Overview, KeySpec


# -------------------------
#  INLINE MODELS (Overview + KeySpec)
# -------------------------
class OverviewInline(admin.TabularInline):
    model = Overview
    extra = 1


class KeySpecInline(admin.TabularInline):
    model = KeySpec
    extra = 1


# -------------------------
#  PHONE ADMIN
# -------------------------
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")
    
    inlines = [OverviewInline, KeySpecInline]


# -------------------------
#  BRAND ADMIN
# -------------------------
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


# -------------------------
#  REGISTER MODELS
# -------------------------
admin.site.register(Brand, BrandAdmin)
admin.site.register(Phone, PhoneAdmin)