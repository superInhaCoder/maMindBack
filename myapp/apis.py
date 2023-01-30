from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from myapp.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from myapp.services import jwt_login, user_get_or_create, set_user_profile
from myapp.exceptions import ServiceUnavailable, DataTypeIncorrect, GoogleAuthError
import requests, json, datetime, jwt

JWT_authenticator = JWTAuthentication()

class MyView(APIView):
    def get(self,request):
        return JsonResponse({'test':'test'})
        raise DataTypeIncorrect
       
class GoogleLoginView(APIView):
        permission_classes = [AllowAny]

        def post(self, request):
                try: token = request.data["token"]
                except KeyError: raise DataTypeIncorrect
                url = 'https://oauth2.googleapis.com/tokeninfo?id_token='
                response = requests.get(url+token)
                accept_status = response.status_code
                if accept_status != 200: raise GoogleAuthError
                
                try:
                    user_json = response.json()
                    user_data = {
                            'sub'           : user_json['sub'],
                            'social'        : 'Google',
                            'email'         : user_json['email'],
                            'name'          : user_json['name'],
                            'last_login'    : datetime.datetime.now(),
                    }
                except: raise GoogleAuthError
                
                user, newUser = user_get_or_create(**user_data)
                token = jwt_login(user=user)
                print(token)
                return JsonResponse({**token, 'newUser' : newUser})


class UserView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 정보 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse(UserSerializer(user).data)

        # 유저 정보 업데이트
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                set_user_profile(user=user, **request.data)
                return JsonResponse({'good': 'good'})
            
class UserCheckView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 체크리스트 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse({'dd': 'dd'})

        # 유저 체크리스트 업데이트
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse({'dd': 'dd'})