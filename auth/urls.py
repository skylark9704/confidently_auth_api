from django.urls import path
from auth.views import ListUsers, Login, GoogleSignIn
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users', ListUsers.as_view()),
    path('auth/login', Login.as_view()),
    path('auth/google/signin', GoogleSignIn.as_view()),
    path('token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('token/verify', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
