from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer
from doctor.models import Doctor
from patient.models import Patient


class RegisterSerializer(RestAuthRegisterSerializer):
    is_doctor = serializers.BooleanField(default=True)

    def custom_signup(self, request, user):
        is_doctor = self.validated_data.get('is_doctor', False)
        if is_doctor:
            doctor = Doctor()
            doctor.user = user
            doctor.save()
        else:
            patient = Patient()
            patient.user = user
            patient.save()
        
