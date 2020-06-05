from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place


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
