from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from myapp.apis import GoogleLoginView, MyView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin', admin.site.urls),
    
    path('login/google', GoogleLoginView.as_view()),
    path('user', UserView.as_view()),
    
    path('', MyView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]