from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from doctor.models import Doctor, DoctorBusyPeriod


# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)


class DoctorAppointment(DoctorBusyPeriod):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

