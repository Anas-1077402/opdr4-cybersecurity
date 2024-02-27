from django.contrib.auth.backends import ModelBackend
from .models import Beheerders

class BeheerdersAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Beheerders.objects.get(username=username)
        except Beheerders.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
