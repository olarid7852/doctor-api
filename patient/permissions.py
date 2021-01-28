from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Patient


class IsPatient(IsAuthenticated):

    def has_permission(self, request, view):
        if super(IsPatient, self).has_permission(request, view):
            return Patient.objects.filter(user=request.user).count() == 1
