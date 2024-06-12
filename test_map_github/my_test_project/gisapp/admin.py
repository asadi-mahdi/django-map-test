from django.contrib import admin

from . import models


class CitiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Cities, CitiesAdmin)
