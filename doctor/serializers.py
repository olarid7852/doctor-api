from rest_framework import serializers
from .models import Doctor, DoctorBlockedOffPeriod

class DoctorBlockedOffPeriodSerializer(serializers.ModelSerializer):
    doctor = None
    class Meta:
        model = DoctorBlockedOffPeriod
        fields = ('start', 'end')
    
    def get_doctor(self):
        if not self.doctor:
            self.doctor = Doctor.objects.get(user=self.context.get('request').user)
        return self.doctor

    def validate_start(self, value):
        if self.get_doctor().doctorbusyperiod_set.filter(start__lte=value).filter(end__gte=value).count() > 0:
            raise serializers.ValidationError("Start time overlap with another period")
        return value
    
    def validate_end(self, value):
        if self.get_doctor().doctorbusyperiod_set.filter(start__lte=value).filter(end__gte=value).count() > 0:
            raise serializers.ValidationError("End time overlap with another period")
        return value

    def validate(self, data):
        start = data['start']
        end = data['end']
        if start > end:
            raise serializers.ValidationError("End time can't be earlier than starting time")
        return data
    
    def save(self, **kwargs):
        # import pudb; pudb.set_trace()
        kwargs['doctor'] = self.get_doctor()
        super(DoctorBlockedOffPeriodSerializer, self).save(**kwargs)