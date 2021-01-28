from rest_framework import routers
from .views import DoctorAppointmentViewSet

router = routers.SimpleRouter()
router.register('appointments', DoctorAppointmentViewSet, basename='appointments')

urlpatterns = router.urls