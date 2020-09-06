from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, PlaceImage
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_places_urls(url):
    base_url = 'https://raw.githubusercontent.com/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    place_urls_tags = soup.select('tbody a')

    places_urls = [
        urljoin(base_url, tag['href'].replace('blob/', ''))
        for tag in place_urls_tags if '.json' in tag['href']
    ]
    return places_urls


def add_images(place, images_urls):
    for order_number, image_url in enumerate(images_urls):
        response = requests.get(image_url)
        response.raise_for_status()
        image, created = PlaceImage.objects.get_or_create(place=place, order_number=order_number)
        name = image_url.split('/')[-1]
        image.image.save(name, ContentFile(response.content), save=True)


def add_place_instance(place_url):
    response = requests.get(place_url)
    response.raise_for_status()
    new_place = response.json()
    images_urls = new_place['imgs']
    place, created = Place.objects.get_or_create(
        title=new_place['title'],
        description_short=new_place['description_short'],
        description_long=new_place['description_long'],
        latitude=new_place['coordinates']['lat'],
        longitude=new_place['coordinates']['lng']
    )
    add_images(place, images_urls)
    return place


class Command(BaseCommand):
    help = 'Uploads places data from json'

    def add_arguments(self, parser):
        parser.add_argument('places_github_url', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            url = options['places_github_url'][0]
            places_urls = fetch_places_urls(url)
            for place_url in places_urls:
                new_place = add_place_instance(place_url)
                self.stdout.write(self.style.NOTICE('Added place: "%s"' % new_place.title))
            self.stdout.write(self.style.SUCCESS('Successfully added places from %s' % url))
        except Exception as error:
            raise CommandError(error)

