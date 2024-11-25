from rest_framework.serializers import ModelSerializer
from testapp.models import *
class AppointmentSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'