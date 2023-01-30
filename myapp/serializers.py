from myapp.models import User, UserCheck, UserGoal
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