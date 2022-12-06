import json

from django.shortcuts import render, get_object_or_404
from .models import Place, Image
from django.http import HttpResponse


def index(request):
    features = []
    detailsUrl = ['../static/moscow_legends.json', '../static/roofs24.json']
    all_places = Place.objects.all()
    for place in all_places:
        feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.short_title,
                    "placeId": place.place_id,
                    "detailsUrl": detailsUrl[0]
                }
                }
        features.append(feature)

    context = {"saved_places": 
        {
        "type": "FeatureCollection",
        "features": features
        }
    }
    return render(request, "index.html", context=context)


def get_json_api(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_imgs = place.images.all()
    context = {
        "title": place.title,
        "imgs": [image.get_absolute_image_url for image in place_imgs],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return HttpResponse(
        json.dumps(context, ensure_ascii=False, indent=2),
        content_type="application/json"
    )