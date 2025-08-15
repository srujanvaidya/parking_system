from django.urls import path
from .views import Parking

urlpatterns=[
    path('park/',Parking.as_view())

]