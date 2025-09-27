from django.contrib.auth.models import User
from django.db import models
from django.utils.traslation import gettext_lazy as _


class CustomUser(User):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

