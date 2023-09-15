from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from django.utils import timezone
from django.conf import settings


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        if not token.user.is_superuser and token.created < timezone.now() - timezone.timedelta(minutes=settings.TOKEN_EXPIRED_MINUTES):
            token.delete()
            raise exceptions.AuthenticationFailed(_('Token has expired.'))

        return (token.user, token)
