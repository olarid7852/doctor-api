import factory
import faker
import random
from datetime import timedelta
from django.utils import timezone

from doctor.factories import DoctorFactory
from user.factories import UserFactory
from .models import Patient, DoctorAppointment

fake = faker.Faker()


class PatientFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Patient


class DoctorAppointmentFactory(factory.django.DjangoModelFactory):
    doctor = factory.SubFactory(DoctorFactory)
    patient = factory.SubFactory(PatientFactory)
    start = timezone.now() + timedelta(minutes=random.randint(1, 10) * 10)
    end = timezone.now() +  + timedelta(minutes=100 + random.randint(1, 10) * 10)

    class Meta:
        model = DoctorAppointment
        