from django.contrib.gis.db import models
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class Cities(models.Model):
    gid = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    center = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    geometry = models.PolygonField(srid=4326, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AreaGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        # another way for validation
        # extra_kwargs = {'name': {'required': True}, 'geometry': {'required': True}}


class AreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Area
        geo_field = "geometry"
        fields = ["id", "name", "created_at"]
