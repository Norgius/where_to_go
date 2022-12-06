from django.contrib import admin
from .models import Place, Image
from  django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    raw_id_fields = ('place', )
    readonly_fields = ['place_img', ]

    def place_img(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url = obj.img.url,
            height='200px',
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_img', ]

    def place_img(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url = obj.img.url,
            height='200px',
            )
        )