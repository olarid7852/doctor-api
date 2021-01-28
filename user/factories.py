import factory
import faker
import random

from . import models


faker = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    username = factory.Sequence(lambda n: faker.user_name() + str(n))
    is_staff = False
    is_active = True

    class Meta:
        model = models.User

