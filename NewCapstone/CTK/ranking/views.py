from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import *
from user.models import *
from django.db.models import F


#분야별 랭킹확인 가능, 점수와 닉네임으로 표기
class RankingView(APIView):
    def get(self, request, category):
        categories = ['Linux', 'Crypto', 'Web', 'System', 'Total']
        
        if category not in categories:
            return Response({'error': 'Invalid category'}, status=status.HTTP_400_BAD_REQUEST)
       
        category_score_field = f'{category.lower()}_score'
        ranking = UserScore.objects.all().order_by(F(category_score_field).desc())

        rankings = [{'user': score.user.nickname, 'score': getattr(score, f'{category.lower()}_score')} for score in ranking]
        
        return Response(rankings)