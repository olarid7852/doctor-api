from django.shortcuts import render
from rest_framework import viewsets
from .models import DoctorBlockedOffPeriod
from .permissions import IsDoctor
from .serializers import DoctorBlockedOffPeriodSerializer

# Create your views here.

class DoctorBlockedOffPeriodViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorBlockedOffPeriodSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        return DoctorBlockedOffPeriod.objects.filter(doctor__user=self.request.user).order_by('start')