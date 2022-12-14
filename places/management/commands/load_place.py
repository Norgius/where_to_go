import os
import sys
from hashlib import md5
from urllib.parse import urlsplit

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from places.models import Place, Image


def get_imagetitle(link):
    parsed_link = urlsplit(link)
    return os.path.split(parsed_link.path)[1]


class Command(BaseCommand):
    help = '''Загружает данные в БД по переданной ссылке, \
              ссылка должна содержать json-файл.'''

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Ссылка на json-файл.')

    def handle(self, *args, **options):
        link = options.get('link')
        try:
            response = requests.get(link)
            response.raise_for_status()
            data_json = response.json()
            images_links = data_json.get('imgs')
            place, new_place = Place.objects.get_or_create(
                title=data_json.get('title'),
                defaults={
                    'description_short': data_json.get('description_short'),
                    'description_long': data_json.get('description_long'),
                    'lng': data_json.get('coordinates').get('lng'),
                    'lat': data_json.get('coordinates').get('lat'),
                }
            )
            place = place if place else new_place
        except requests.exceptions.HTTPError as http_er:
            sys.stderr.write(f'\n Ошибка загрузки json-файла.\n{http_er}\n\n')
            return
        for image_link in images_links:
            try:
                response = requests.get(image_link)
                response.raise_for_status()
                content = response.content
                content_img = ContentFile(content, name=md5(content).hexdigest())
                Image.objects.create(place=place, img=content_img)
            except requests.exceptions.HTTPError as http_er:
                sys.stderr.write(
                    f'\n Ошибка загрузки изображения\n{http_er}\n\n')
                continue
        sys.stdout.write(f'\n{place.title} добавлено в БД.\n')