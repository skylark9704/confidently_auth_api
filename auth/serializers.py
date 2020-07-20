from rest_framework_simplejwt.tokens import RefreshToken


class SignToken(RefreshToken):

    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)

        # Add custom claims
        token['email'] = user.email
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name

        return token
