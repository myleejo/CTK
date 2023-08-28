from rest_framework import serializers
from .models import Problem

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['problem_id', 'title', 'score', 'category']


class ProblemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['title', 'contents', 'score', 'category', 'ssh_path']

class ProblemAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['problem_id', 'title', 'score', 'category', 'contents', 'flag', 'ssh_path']