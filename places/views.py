from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place, PlaceImage
from django.shortcuts import get_object_or_404
from django.urls import reverse


def make_feature_for_geojson(place):
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude],
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse(place_detail, args=[place.pk]),
        }
    }
    return feature


def index(request):
    places = Place.objects.all()

    places_geojson = {
        "type": "FeatureCollection",
        "features": [],
    }

    for place in places:
        feature = make_feature_for_geojson(place)
        places_geojson["features"].append(feature)

    context = {
        "places_geojson": places_geojson,
    }

    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    serialized_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude
        }
    }

    return JsonResponse(serialized_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
