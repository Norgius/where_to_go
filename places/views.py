from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.urls import reverse
from .models import Place


def index(request):
    features = []
    all_places = Place.objects.all()
    for place in all_places:
        feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('place-detail', args=(place.id, ))
                },
        }
        features.append(feature)

    context = {
        "saved_places": {
            "type": "FeatureCollection",
            "features": features,
        },
    }
    return render(request, "index.html", context=context)


def get_place_detail(request, identifier):
    place = get_object_or_404(Place, id=identifier)
    context = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        },
    }
    return JsonResponse(
        context,
        json_dumps_params={'indent': 2, 'ensure_ascii': False},
    )
