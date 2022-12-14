from django.utils.safestring import mark_safe


def place_img(image):
    return mark_safe('<img src="{url}" height={height} />'.format(
        url=image.img.url,
        height='200px',
        )
    )
