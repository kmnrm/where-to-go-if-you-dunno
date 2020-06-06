from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.safestring import mark_safe
from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
	model = PlaceImage
	fields = ['image', 'get_preview']
	readonly_fields = ['get_preview']
	extra = 0

	def get_preview(self, place):
		return mark_safe('<img src="{url}" height="200" />'.format(url=place.image.url))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	inlines = [
		PlaceImageInline,
	]
