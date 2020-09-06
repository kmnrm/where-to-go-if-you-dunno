from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Подробное описание', blank=True)
    #to pelid: тогда почему в уроке про риэлтора в django orm у вас поле называется owner_phone_pure, а не owner_pure_phone_number?
    # https://dvmn.org/modules/django-orm/lesson/filtering-products/#13
    latitude = models.FloatField('Координаты широты')
    longitude = models.FloatField('Координаты долготы')

    def __str__(self):
        return f"{self.title}"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    order_number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.order_number} {self.place.title}"

    class Meta:
        ordering = ['order_number']
