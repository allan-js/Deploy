from django.contrib import admin
from .models import Staff, Meal, Banner, GalleryImage, Room, BaseInfo, Document


class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')
    search_fields = ('full_name',)


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    list_filter = ('is_active', 'created')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'created')
    list_filter = ('is_active',)


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    list_per_page = 50
    list_filter = ('created', 'is_active')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)

class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(BaseInfo, BaseInfoAdmin)
admin.site.register(Document, DocumentAdmin)
