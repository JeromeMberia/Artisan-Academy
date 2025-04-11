from django.contrib import admin
from .models import ArtisanProfile

@admin.register(ArtisanProfile)
class ArtisanProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "experience_years", "created_at")
    search_fields = ("full_name", "user__email")
    list_filter = ("experience_years",)

