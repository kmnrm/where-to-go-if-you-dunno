import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place, PlaceImage
from django.shortcuts import get_object_or_404


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
			"detailsUrl": "static/places/roofs24.json",
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
		print(place.title)
		feature = make_feature_for_geojson(place)
		places_geojson["features"].append(feature)

	context = {
		"places_geojson": places_geojson,
	}

	return render(request, 'index.html', context)


def place_detail(request, place_id):
	place = get_object_or_404(Place, pk=place_id)
	place_images = PlaceImage.objects.filter(place__pk=place_id)

	serialized_place = {
		"title": "Экскурсионная компания «Легенды Москвы»",
		"imgs": [image.image.url for image in place_images],
		"description_short": place.description_short,
		"description_long": place.description_long,
		"coordinates": {
			"lat": place.latitude,
			"lng": place.longitude
		}
	}

	return JsonResponse(serialized_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
