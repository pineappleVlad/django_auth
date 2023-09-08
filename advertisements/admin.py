from django.contrib import admin
from .models import Advertisement

# @admin.register(AdvertisementStatusChoices)
# class AdvertisementStatusChoicesAdmin(admin.ModelAdmin):
#     list_display = ['OPEN', 'CLOSED']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator', 'created_at', 'updated_at']
