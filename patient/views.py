from django.shortcuts import render
from rest_framework import viewsets
from .models import DoctorAppointment
from .permissions import IsPatient
from .serializers import DoctorAppointmentSerializer

# Create your views here.

class DoctorAppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAppointmentSerializer
    permission_classes = [IsPatient]

    def get_queryset(self):
        return DoctorAppointment.objects.filter(patient__user=self.request.user).order_by('start')
