# # user/authentication.py

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from user.models import CustomToken
# from django.utils import timezone

# class CustomTokenAuthentication(TokenAuthentication):
#     def authenticate_credentials(self, key):
#         try:
#             token = CustomToken.objects.get(key=key)
#         except CustomToken.DoesNotExist:
#             raise AuthenticationFailed('Invalid token')

#         if token.expire_date < timezone.now():
#             raise AuthenticationFailed('Token has expired')

#         return token.user, token
