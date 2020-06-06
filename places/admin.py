from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
	model = PlaceImage
	fields = ['image', 'get_preview', 'order_number']
	readonly_fields = ['get_preview']

	def get_preview(self, place):
		return mark_safe('<img src="{url}" height="200" />'.format(url=place.image.url))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	inlines = [
		PlaceImageInline,
	]
