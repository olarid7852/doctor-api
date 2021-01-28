import faker
from django.test import TestCase
from django.urls import reverse
from doctor.models import Doctor
from patient.models import Patient
from rest_framework.test import APITestCase
from rest_framework import status
from doctor.factories import DoctorFactory
from patient.factories import PatientFactory
from . import factories
from doctor.models import Doctor
from patient.models import Patient


faker = faker.Faker()
# Create your tests here.


class RegistrationApiTest(APITestCase):
    url = reverse('rest_register')
    def test_create_doctor(self):
        """
        Ensure we can create a new account object.
        """
        test_password = 'ooooooooooooooooooooooo'
        username = faker.first_name()
        data = {'username': username, 'email': faker.email(), 'password1': test_password, 'password2': test_password, 'is_doctor': True}
        response = self.client.post(self.url, data, format='json')
        # import pudb; pudb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')

    def test_create_patient(self):
        test_password = 'ooooooooooooooooooooooo'
        username = faker.first_name()
        data = {'username': username, 'email': faker.email(), 'password1': test_password, 'password2': test_password, 'is_doctor': False}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)


class DoctorPermissionTest(APITestCase):
    
    def setUp(self):
        super(DoctorPermissionTest, self).setUp()
        doctor = DoctorFactory()
        self.doctor = doctor
        self.user = self.doctor.user
        self.client.force_authenticate(user=self.user)
    
    def test_permisssion_denied_for_patient_appointment_list(self):
        response = self.client.get(reverse('appointments-list'), format='json')
        self.assertEqual(response.status_code, 403)


class PatientPermissionTest(APITestCase):
    
    def setUp(self):
        super(PatientPermissionTest, self).setUp()
        patient = PatientFactory()
        self.patient = patient
        self.user = self.patient.user
        self.client.force_authenticate(user=self.user)

    def test_permisssion_denied_for_doctor_blocked_off_period_list(self):
        response = self.client.get(reverse('doctor-time-off-list'), format='json')
        self.assertEqual(response.status_code, 403)