"""
URL configuration for CTK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from problem.views import *
from ranking.views import *


router = DefaultRouter()
router.register(r'problems', ProblemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('problem/', include('problem.urls')),
    
    #유저관련(로그인, 회원가입, 프로필...) user urls.py에서 확인가능
    path('user/', include('user.urls')), 

    path('ranking/', include('ranking.urls')),
    path('api/', include(router.urls)),
    path('password/', include('django.contrib.auth.urls')),
    
    # 문제관련
    path('api/problems/<int:problem_id>/', ProblemDetailView.as_view(), name='problem-detail'),
    path('api/problems/<int:problem_id>/check-flag/', CheckFlagView.as_view(), name='check-flag'), 
    path('api/problems/category/<str:category>/', ProblemListView.as_view(), name='problem-list-by-category'), #분야별 문제 리스트
    path('api/problems/', ProblemListView.as_view(), name='problem-list'), # 전체 문제 리스트 
    
    #랭킹관련
    path('api/ranking/<str:category>/', RankingView.as_view(), name='api-ranking'), #분야별 랭킹
]


