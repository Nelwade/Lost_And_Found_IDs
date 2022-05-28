from django.contrib import admin
from .models import Id_item
from django.utils.html import format_html
# Register your models here.
class ID_Admin(admin.ModelAdmin):
    search_fields = ['ID_num']
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="300px" height = "200px"/>'.format(obj.Image.url))

    image_tag.short_description = 'Image'

    list_display = ['ID_num', 'Find_Date']
    readonly_fields = ['image_tag', 'ID_num', 'Location_found']

admin.site.register(Id_item, ID_Admin)