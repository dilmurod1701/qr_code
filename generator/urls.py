from django.urls import path

from . import views

urlpatterns = [
    path('<str:wifi_name>/<str:password>/<str:encryption>', views.generate),
]
