from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if (obj.image_field == ""):
            return "Нет изображения"
        return format_html('<img src="{}" width="100" />'.format(obj.image_field.url))

    image_tag.short_description = 'изображение'

    list_display = ['image_tag', '__str__', 'image_field', 'date_create', 'date_update']
    list_display_links = ['__str__']


admin.site.register(models.Book, BookAdmin)