from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('/', views.home_page),
    path('/register', views.register),
    path('/cities', views.cities),
    path('/about', views.example_view),
    path('/api-token-auth', auth_views.obtain_auth_token),
    path('/area', views.create_area),
    path('/area/<int:id>', views.find_area),
    path('/area/find-all', views.find_all_areas),
    path('/area/<int:id>', views.update_area),
]
