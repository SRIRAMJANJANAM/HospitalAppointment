from django.urls import path,include
from rest_framework import routers
from testapp.api.views import AppointmentCRUDCBV
router=routers.DefaultRouter()
router.register('Appointment',AppointmentCRUDCBV)
urlpatterns=[
    path('',include(router.urls))
]