from django.urls import path

from . import views

urlpatterns = [
    path('/', views.members),
    path('/rest-response', views.rest_response),
    path('/create', views.create),
    path('/find/<int:id>', views.find_member),
    path('/find-all', views.find_all),
    path('/update', views.update),
    path('/delete/<int:id>', views.delete),
]
