from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from jdatetime import datetime as jalali_date_time
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from .forms import NewUserForm
from .models import AreaSerializer, AreaGeneralSerializer

from test_map_github.my_test_project.my_test_project.exceptions import custom_exception_handler


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
@transaction.atomic()
def create_area(request):
    try:
        serializer = AreaGeneralSerializer(data=request.data)
        detail_of_serializer = repr(serializer)
        if serializer.is_valid():
            import traceback
            name = request.data.get("name")
            geometry = GEOSGeometry(str(request.data.get("geometry")))
            area = models.Area(name=name, geometry=geometry)
            area.save()
            s = traceback.format_exc()
            # g = GEOSGeometry(request.data.get("geometry"))
            return Response(area.id)
        return custom_exception_handler(serializer.errors, context="validation")
    except Exception as e:
        return custom_exception_handler(e, context="view")


@api_view(["GET"])
def find_area(request, id):
    try:
        # a = request.META['sso']

        # # with filter()
        # area = models.Area.objects.filter(id=id)
        # created_at_jalali = jalali_date_time.fromgregorian(datetime=area.values()[0].get("created_at")).strftime(
        #     "%Y/%m/%d, %H:%M")
        # result = AreaSerializer(area.values()[0]).data
        # result["properties"]["created_at"] = created_at_jalali

        # # with get()
        area = models.Area.objects.get(id=id)
        created_at_jalali = jalali_date_time.fromgregorian(datetime=area.created_at).strftime("%Y/%m/%d, %H:%M")
        result = AreaSerializer(area).data
        result["properties"]["created_at"] = created_at_jalali
        return Response(result)
    except BaseException as e:
        return custom_exception_handler(e, context="view")


@api_view(["GET"])
def find_all_areas(request):
    try:
        areas = models.Area.objects.all()
        return Response(AreaSerializer(areas, many=True).data)
    except Exception as e:
        return custom_exception_handler(e, context="view")


@api_view(["PUT"])
def update_area(request, id):
    try:
        area = models.Area.objects.get(id=id)
        serializer = models.AreaGeneralSerializer(data=request.data)
        if serializer.is_valid():
            # check name not repetitive
            if area.name != request.data.get("name"):
                area2 = models.Area.objects.filter(name=request.data.get("name"))
                if area2.count() > 0:
                    if area2.first().name == request.data.get("name"):
                        raise ParseError(detail="محدوده ای با این عنوان وجود دارد")
            area.name = request.data.get("name")
            area.geometry = GEOSGeometry(str(request.data.get("geometry")))
            area.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return custom_exception_handler(e, context="view")


@api_view(["DELETE"])
def delete_area(request, id):
    try:
        area = models.Area.objects.get(id=id)
        return Response(area.delete())
    except Exception as e:
        return custom_exception_handler(e, context="view")

# @api_view(["POST"])
# def search(request):
#     try:
#         serializer = models.GisOsmPoisFree1RequestSerializer(data=request.data)
#         if serializer.is_valid():
#             geometry = GEOSGeometry(str(request.data.get("geom")))
#             name = request.data.get("name")
#             result = {}
#             if geometry.geom_type == "Polygon":
#                 result = models.Gis_osm_pois_free_1.objects.filter(geom__intersects=geometry,
#                                                                    name__contains=name)
#             elif geometry.geom_type == "Point":
#                 result = (models.Gis_osm_pois_free_1.objects
#                           .annotate(distance=Distance('geom', geometry))
#                           .filter(distance__lte=1000, name__contains=name)
#                           .order_by('distance'))
#             return Response(models.GisOsmPoisFree1Serializer(result, many=True).data)
#         return custom_exception_handler(serializer.errors, context="validation")
#     except Exception as e:
#         return custom_exception_handler(e, context="view")
