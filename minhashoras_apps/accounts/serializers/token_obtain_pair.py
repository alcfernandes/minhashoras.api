from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if not user.account:
            raise exceptions.AuthenticationFailed(
                _('The user does not belong to any account.')
            )

        token = super().get_token(user)

        token['account_uuid'] = str(user.account.uuid)

        return token
