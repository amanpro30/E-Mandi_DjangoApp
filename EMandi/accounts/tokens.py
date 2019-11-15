from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.userprofile.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()