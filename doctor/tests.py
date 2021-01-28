import faker
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from doctor.models import Doctor
from patient.models import Patient
from rest_framework.test import APITestCase
from rest_framework import status
from .factories import DoctorFactory, DoctorBlockedOffFactory
from .models import DoctorBlockedOffPeriod
from doctor.models import Doctor
from patient.models import Patient
from datetime import datetime, timedelta

# Create your tests here.
class TestDoctorBlockedPeriodCreateApi(APITestCase):
    url = reverse('doctor-time-off-list')
    def setUp(self):
        super(TestDoctorBlockedPeriodCreateApi, self).setUp()
        doctor = DoctorFactory()
        self.user = doctor.user
        self.doctor = doctor
        self.client.force_authenticate(user=self.user)

    def test_set_block_off_period(self):
        start = timezone.now()
        end = start + timedelta(hours=1)
        data = {'start': start, 'end': end}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(DoctorBlockedOffPeriod.objects.count(), 1)
        obj = DoctorBlockedOffPeriod.objects.get(pk=1)
        self.assertEqual(start.timestamp(), obj.start.timestamp())
        self.assertEqual(end.timestamp(), obj.end.timestamp())
        self.assertEqual(self.doctor, obj.doctor)


    def test_reject_overlapping_blocked_off_period(self):
        start = datetime.now() + timedelta(hours=2)
        end = start + timedelta(hours=1)
        data = {'start': start, 'end': end}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(201, response.status_code)

        data = {'start': start + timedelta(minutes=5), 'end': end - timedelta(minutes=5)}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)
        

    def test_end_time_must_be_higher_than_start_time(self):
        start = datetime.now() + timedelta(hours=10)
        end = start - timedelta(minutes=5)
        data = {'start': start, 'end': end}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(400, response.status_code)


def TestDoctorBlockedupPeriodListApi(APITestCase):
    url = reverse('doctor-time-off-list')
    def setUp(self):
        super(TestDoctorBlockedupPeriodListApi, self).setUp()
        doctor = DoctorFactory()
        self.user = doctor.user
        self.client.force_authenticate(user=self.user)

    def test_can_see_only_my_blocked_periods(self):
        DoctorBlockedOffFactory.create_batch(10)
        DoctorBlockedOffFactory.create_batch(10, doctor=self.doctor)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(len(response.json['result']), 8)