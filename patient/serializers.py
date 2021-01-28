from rest_framework import serializers
from doctor.models import Doctor, DoctorBlockedOffPeriod
from .models import Patient, DoctorAppointment

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    patient = None
    class Meta:
        model = DoctorAppointment
        fields = ('start', 'end', 'doctor')

    def get_patient(self):
        if not self.patient:
            self.patient = Patient.objects.get(user=self.context.get('request').user)
        return self.patient
    
    def validate(self, data):
        doctor = data['doctor']
        start = data['start']
        end = data['end']
        if start > end:
            raise serializers.ValidationError("Start time can't be after end time.")
        if not doctor.check_if_free(start, end):
            raise serializers.ValidationError("Doctor is busy at this time.")
        return data

    def save(self, **kwargs):
        kwargs['patient'] = self.get_patient()
        super(DoctorAppointmentSerializer, self).save(**kwargs)