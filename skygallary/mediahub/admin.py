from django.contrib import admin

# Register your models here.
from .models import PhotoAsset

# admin.site.register(PhotoAsset)

@admin.register(PhotoAsset)
class PhotoAssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    
