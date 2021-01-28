from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Doctor


class IsDoctor(IsAuthenticated):

    def has_permission(self, request, view):
        if super(IsDoctor, self).has_permission(request, view):
            return Doctor.objects.filter(user=request.user).count() == 1
