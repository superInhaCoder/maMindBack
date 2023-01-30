from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from myapp.apis import GoogleLoginView, MyView, UserView, TestLoginView, UserGoalView, UserCheckView, TestListView, UserCheckCalView, TestItemView
from myapp.apis import GoalListView, GoalCategoryView
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
    path('login/test', TestLoginView.as_view()),
    path('user', UserView.as_view()),
    path('user/check', UserCheckView.as_view()),
    path('user/goal', UserGoalView.as_view()),
    path('testlist', TestListView.as_view()),
    path('testitem', TestItemView.as_view()),
    path('goallist', GoalListView.as_view()),
    path('goalcategory', GoalCategoryView.as_view()),
    path('user/check/cal', UserCheckCalView.as_view()),
    
    path('', MyView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]