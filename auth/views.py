from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from auth.lib.helpers.request import get_access_token_from_request
import jwt
from auth.serializers import SignToken
from auth.lib.helpers.google_oauth import get_google_user_details


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        # Testing Decode from module:jwt
        decoded = jwt.decode(
            get_access_token_from_request(request), None, None)
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class Login(APIView):

    def post(self, request):

        # Get credentials from request
        credentials = request.data

        # Find User
        try:
            user = User.objects.get(username=credentials['username'])
        except User.DoesNotExist:
            return Response({'error': 'User does not exits'})

        if user.check_password(raw_password=credentials['password']):

            # Sign JWT
            refresh = SignToken.for_user(user)

            payload = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'email': user.email,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }

            return Response(payload)

        return Response({'error': 'Authentication Failed'})


class GoogleSignIn(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        code = request.data['code']
        user = get_google_user_details(request=request, code=code)
        return Response(user)
