from django.contrib.gis.db import models


class Cities(models.Model):
    gid = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    center = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
