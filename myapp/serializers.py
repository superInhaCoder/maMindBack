from myapp.models import User, UserCheck, UserGoal, TestList, Doctor, Consult, Doctor, GoalList, GoalCategory
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UserCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCheck
        fields = "__all__"
        
class UserGoalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGoal
        fields = "__all__"
        
class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestList
        fields = "__all__"
        
class TestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestList
        fields = "__all__"
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        
class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = "__all__"
        
class GoalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalList
        fields = "__all__"
        
class GoalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalCategory
        fields = "__all__"