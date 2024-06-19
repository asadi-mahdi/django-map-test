from django.utils import timezone

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jdatetime import datetime as jalali_date_time

from . import models
from .forms import NewUserForm


@login_required(login_url='/accounts/login/')
def home_page(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        form = NewUserForm()
        return render(request, 'registration/register.html', context={"register_form": form})
    elif request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/gisapp")
        else:
            return redirect("/gisapp/register")


@api_view(['GET'])
def cities(request):
    try:
        # all = models.Cities.objects.all()[85]
        # a = ogr.open()
        # outputFolderPath = "C:\\Users\\dev25\\Desktop\\Django\\django-test\\my_test_project\\"
        # writeTIF = outputFolderPath + 'sample.tif'  # filename with new tif extension
        # tiff_ds = gdal.GetDriverByName('GTiff')
        # tiff_ds.Create(writeTIF, 1024, 1024, 1, gdal.GDT_UInt16, options=['PROFILE=GeoTIFF'])
        #
        # # Rasterize
        # ds = gdal.RasterizeLayer(tiff_ds, [1], a, burn_values=[200], options=["ALL_TOUCHED=TRUE"])

        city = models.Cities.objects.filter(name="تهران")
        city2 = models.Cities.objects.get(name="كرمان")
        # gdal.RasterizeLayer("tehran.tif", [1], all.geom, burn_values=[1], options=['ALL_TOUCHED=TRUE'])
        # return raster
        return Response(serialize("geojson", city, geometry_field="geom"))
    except Exception as e:
        raise ParseError(detail=e)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


@api_view(["POST"])
def create_area(request):
    try:
        name = request.data.get("name")
        geometry = GEOSGeometry(str(request.data.get("geometry")))
        area = models.Area(name=name, geometry=geometry)
        area.save()
        return Response(area.id)
    except Exception as e:
        raise ParseError(detail=e)


@api_view(["GET"])
def find_area(request, id):
    try:
        a = request.META['sso']
        area = models.Area.objects.filter(id=id)
        aa = area.values("updated_at")[0].get("updated_at")
        result = {

            "update time": jalali_date_time.fromgregorian(datetime=area.values("updated_at")[0].get("updated_at")).strftime("%Y/%m/%d, %H:%M")
        }
        return Response(serialize('geojson', area))
    except Exception as e:
        raise ParseError(detail=e)
