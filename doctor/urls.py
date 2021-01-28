from rest_framework import routers
from .views import DoctorBlockedOffPeriodViewSet

router = routers.SimpleRouter()
router.register('timeOff', DoctorBlockedOffPeriodViewSet, basename='doctor-time-off')

urlpatterns = router.urls