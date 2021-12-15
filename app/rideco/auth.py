from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.utils.translation import gettext_lazy as _



class CustomAuth(JWTAuthentication):

    def get_validated_token(self, raw_token):
            """
            Validates an encoded JSON web token and returns a validated token
            wrapper object.
            """
            messages = []
            for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
                try:
                    print(raw_token)
                    return AuthToken(raw_token)
                except TokenError as e:
                    print('before append')
                    messages.append({'token_class': AuthToken.__name__,
                                    'token_type': AuthToken.token_type,
                                    'message': e.args[0]})
            print('Here we are')
            raise InvalidToken({
                'detail': _('Given token not valid for any token type'),
                'messages': messages,
            })