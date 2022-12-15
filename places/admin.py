from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from places.download_tools import show_image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    raw_id_fields = ('place', )
    readonly_fields = ['place_img', ]

    def place_img(self, image):
        return show_image(image)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline, ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_img', ]

    def place_img(self, image):
        return show_image(image)
