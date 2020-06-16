from django.contrib import admin
from .models import City


# admin.site.register(City)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = ('name', 'created',)
