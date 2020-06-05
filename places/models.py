from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Подробное описание', blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.title}"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    order_number = models.IntegerField()

    def __str__(self):
        return f"{self.order_number} {self.place.title}"
