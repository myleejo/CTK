from rest_framework import serializers
from .models import *
from ranking.models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname']

class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['crypto_score', 'linux_score', 'web_score', 'system_score', 'total_score']