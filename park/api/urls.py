from django.urls import path
from .views import Parkingsys


urlpatterns=[
    path('park/',Parkingsys.as_view())

]