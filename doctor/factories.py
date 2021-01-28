import factory
import faker
import random
from datetime import timedelta
from django.utils import timezone
from user.factories import UserFactory
from .models import Doctor, DoctorBlockedOffPeriod

fake = faker.Faker()


class DoctorFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Doctor


class DoctorBlockedOffFactory(factory.django.DjangoModelFactory):
    doctor = factory.SubFactory(DoctorFactory)
    start = timezone.now() + timedelta(minutes=random.randint(1, 10) * 10)
    end = timezone.now() +  + timedelta(minutes=100 + random.randint(1, 10) * 10)

    class Meta:
        model = DoctorBlockedOffPeriod
