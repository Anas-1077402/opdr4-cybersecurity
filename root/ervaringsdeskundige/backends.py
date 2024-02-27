from django.contrib.auth.backends import ModelBackend
from .models import Ervaringsdeskundige

class ErvaringsdeskundigeAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Ervaringsdeskundige.objects.get(username=username)
        except Ervaringsdeskundige.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None