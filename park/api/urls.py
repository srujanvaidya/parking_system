from django.urls import path
from .views import Parkingsys,Parks,Exit#,Parkingdetail

urlpatterns=[
    path('park/',Parkingsys.as_view()),
    #path('park/<str:plate>/',Parkingdetail.as_view())
    path('park/input/',Parks.as_view()),
    path('park/exit/',Exit.as_view())

]