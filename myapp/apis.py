from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from myapp.serializers import UserSerializer, UserCheckSerializer, UserGoalSerializer, TestListSerializer, TestItemSerializer, GoalListSerializer, GoalCategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from myapp.services import jwt_login, user_get_or_create, set_user_profile, get_user_check, create_user_check, get_test_list
from myapp.services import set_user_check, get_test_item, get_user_check_cal, get_goal_list, get_goal_category, create_user_goal
from myapp.services import set_user_goal, get_user_goal, get_user_goal_with_success, get_user_goal_cal, get_goal_list_with_now
from myapp.exceptions import ServiceUnavailable, DataTypeIncorrect, GoogleAuthError
from django.core import serializers
import requests, json, datetime, jwt
from myapp.models import GoalList

JWT_authenticator = JWTAuthentication()

class MyView(APIView):
    def get(self,request):
        return JsonResponse({'test':'test'})
        raise DataTypeIncorrect

class TestLoginView(APIView):
        permission_classes = [AllowAny]
        
        def post(self, request):
                user_data = {
                        'sub'           : 0,
                        'social'        : 'Google',
                        'email'         : 'pkseonguk@gmail.com',
                        'name'          : '관리자',
                        'last_login'    : datetime.datetime.now(),
                }
                
                user, newUser = user_get_or_create(**user_data)
                token = jwt_login(user=user)
                print(token)
                return JsonResponse({**token, 'newUser' : newUser})
        
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
        def patch(self, request):
                user, token = JWT_authenticator.authenticate(request)
                set_user_profile(user=user, **request.data)
                return JsonResponse({'good': 'good'})

class UserCheckView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 체크리스트 생성
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['value'] = ','.join(map(str, data['value']))
                        data['selected_date']
                        data['test_list_id']
                except:
                        raise DataTypeIncorrect
                create_user_check(user, **data)
                return JsonResponse({'good': 'good'})

        # 유저 체크리스트 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse(UserCheckSerializer(get_user_check(user), many=True).data, safe=False)

        # 유저 체크리스트 업데이트
        def patch(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['update']
                except:
                        raise DataTypeIncorrect
                set_user_check(user=user, **request.data)
                return JsonResponse({'good': 'good'})

class UserCheckCalView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 검사 누적 결과
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                userCheckCalDict = get_user_check_cal(user)
                return JsonResponse(userCheckCalDict, safe=False)
        
class UserGoalCalView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 목표 누적 결과
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                userGoalCalDict = get_user_goal_cal(user)
                return JsonResponse(userGoalCalDict, safe=False)
        
class UserGoalView(APIView):
        permission_classes = [IsAuthenticated]

        # 유저 목표 생성
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['goal_id']
                        data['category']
                except:
                        raise DataTypeIncorrect
                d = {'goal_id': data['goal_id']}
                create_user_goal(user, **d)
                return JsonResponse(get_goal_list_with_now(user, **data), safe=False)

        # 유저 목표 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                s = UserGoalSerializer(get_user_goal(user), many=True).data
                # return JsonResponse(s, safe=False)
                for dic in s:
                        dic['data'] = GoalListSerializer(GoalList.objects.filter(id=dic['id']), many=True).data
                return JsonResponse(dic, safe=False)

        # 유저 목표 업데이트
        def patch(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['id']
                        data['update']
                except:
                        raise DataTypeIncorrect
                set_user_goal(user=user, **data)
                
                return JsonResponse({'good': 'good'})
        
class TestListView(APIView):
        permission_classes = [IsAuthenticated]

        # 검사 목록 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse(TestListSerializer(get_test_list(), many=True).data, safe=False)
        
class GoalCategoryView(APIView):
        permission_classes = [IsAuthenticated]

        # 목표 카테고리 반환
        def get(self, request):
                user, token = JWT_authenticator.authenticate(request)
                return JsonResponse(GoalCategorySerializer(get_goal_category(), many=True).data, safe=False)

class GoalListView(APIView):
        permission_classes = [IsAuthenticated]

        # 목표 목록 반환
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['category']
                except:
                        raise DataTypeIncorrect
                        
                return JsonResponse(get_goal_list_with_now(user, **data), safe=False)
        
class TestItemView(APIView):
        permission_classes = [IsAuthenticated]

        # 검사 아이템 반환
        def post(self, request):
                user, token = JWT_authenticator.authenticate(request)
                data = request.data
                try:
                        data['type']
                except:
                        raise DataTypeIncorrect
                d = TestItemSerializer(get_test_item(**data), many=True).data
                
                return JsonResponse(d, safe=False)