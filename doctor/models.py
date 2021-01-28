from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)

    def check_if_free(self, start, end):
        if self.doctorbusyperiod_set.filter(start__lte=start).filter(end__gte=start):
            return False
        if self.doctorbusyperiod_set.filter(start__lte=end).filter(end__gte=end):
            return False
        return True


class DoctorBusyPeriod(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE)
    start = models.DateTimeField(_("Start"), help_text=_("Start time"))
    end = models.DateTimeField(_("End"), help_text=_("End time"))

class DoctorBlockedOffPeriod(DoctorBusyPeriod):
    details = models.CharField(max_length=50)