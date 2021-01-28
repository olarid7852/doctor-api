import faker
from django.test import TestCase
from django.urls import reverse
from doctor.models import Doctor
from django.utils import timezone
from datetime import timedelta
from patient.models import Patient
from rest_framework.test import APITestCase
from rest_framework import status
# from .factories import factories
from doctor.models import Doctor
from doctor.factories import DoctorFactory, DoctorBlockedOffFactory
from .models import Patient, DoctorAppointment
from .factories import PatientFactory, DoctorAppointmentFactory

# Create your tests here.
class TestPatientAppointmentCreateApi(APITestCase):
    url = reverse('appointments-list')

    def setUp(self):
        super(TestPatientAppointmentCreateApi, self).setUp()
        doctor = DoctorFactory()
        self.doctor = doctor
        self.patient = PatientFactory()
        self.user = self.patient.user
        self.client.force_authenticate(user=self.user)


    def test_free_period(self):
        start = timezone.now() + timedelta(hours=10)
        end = start + timedelta(hours=1)
        data = {'start': start, 'end': end, 'doctor': 1}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(DoctorAppointment.objects.count(), 1)
        obj = DoctorAppointment.objects.get(pk=1)
        self.assertEqual(start.timestamp(), obj.start.timestamp())
        self.assertEqual(end.timestamp(), obj.end.timestamp())
        self.assertEqual(self.patient, obj.patient)

    def test_blocked_off_period(self):
        doctor_blocked_off_period = DoctorBlockedOffFactory(doctor=self.doctor)
        data = {'start': doctor_blocked_off_period.start + timedelta(minutes=1), 'end': doctor_blocked_off_period.end - timedelta(minutes=1), 'doctor': 1}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)

    
    def test_end_time_must_be_higher_than_start_time(self):
        start = timezone.now()
        end = start - timedelta(hours=1)
        data = {'start': start, 'end': end, 'doctor': 1}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)


class TestPatientAppointmentList(APITestCase):
    url = reverse('appointments-list')
    def setUp(self):
        doctor = DoctorFactory()
        self.doctor = doctor
        self.patient = PatientFactory()
        self.user = self.patient.user
        self.client.force_authenticate(user=self.user)
    
    def test_that_patient_can_only_see_his_appointments(self):
        DoctorAppointmentFactory.create_batch(10)
        DoctorAppointmentFactory.create_batch(5, patient=self.patient)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['count'], 5)
