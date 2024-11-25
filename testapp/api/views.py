from rest_framework import viewsets
from testapp.api.serializers import AppointmentSerializer
from testapp.models import *
class AppointmentCRUDCBV(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer