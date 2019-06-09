from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

class CustomAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        model = self.get_model()
        try:
            token = auth[1].decode()
            token = model.objects.select_related('user').get(key=token)
            return (token.user, token)

        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(('Invalid token.'))

        return (AnonymousUser(), token)


