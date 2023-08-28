from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *
from .models import Problem
from user.models import *
from ranking.models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ProblemViewSet 보여주기 /api
class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemAllSerializer

    
# class ProblemListView(generics.ListAPIView):
#     serializer_class = ProblemSerializer

#     def get_queryset(self):
#         category = self.request.query_params.get('category')
#         queryset = Problem.objects.all().order_by('problem_id')

#         if category:
#             queryset = queryset.filter(category=category)

#         return queryset


class ProblemListView(generics.ListAPIView):
    serializer_class = ProblemSerializer

    def get_queryset(self):
        category = self.kwargs.get('category')  # URL 매개변수로부터 카테고리 값을 받아옴
        queryset = Problem.objects.all().order_by('problem_id')

        if category:
            queryset = queryset.filter(category=category)

        return queryset
    

class ProblemDetailView(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemDetailSerializer
    lookup_field = 'problem_id'



# 문제 정답시 점수 추가, 이미 맞힌 정답일시 점수추가X
class CheckFlagView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, problem_id):
        problem = get_object_or_404(Problem, problem_id=problem_id)
        user = request.user
        user_score, created = UserScore.objects.get_or_create(user=user)

        user_flag = request.data.get('flag')

        if user_flag == problem.flag:
            if user_score.has_solved(problem):
                return Response({'message': '이미 문제를 해결한 적이 있습니다.', 'score': user_score.total_score}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_score.add_score(problem.score,problem.category)
                user_score.solved_problems.add(problem)
               

                return Response({'message': '문제를 해결하였습니다.', 'score': user_score.total_score}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '틀린 답입니다.', 'score': user_score.total_score}, status=status.HTTP_400_BAD_REQUEST)


# class Main(APIView):
#     def get(self, request):

#         email = request.session.get('email',None)
        
#         if email is None:
#             return render(request,"user/login.html")
        
#         user = User.objects.filter(email=email).first()
        
#         if user is None:
#             return render(request,"user/login.html")

#         return render(request, 'problem/main.html',context=dict(user=user))
    
