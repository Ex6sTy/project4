from rest_freamework.permissions import BasePermissions


class IsOwnerOrStaff(BasePermissions):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return requst.user == view.get_object().owner
