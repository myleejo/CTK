from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import get_user_model, authenticate
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib import messages

from rest_framework.permissions import *
from rest_framework.authentication import *
from rest_framework.authtoken.models import Token

from ranking.models import UserScore

from .serializers import *

# Create your views here.

#회원가입 닉네임, 이메일, 이름, 비밀번호 입력.(닉네임, 이메일 중복불가)
class Join(APIView):
    # def get(self,request):
    #     return render(request,"user/join.html")
    
    def post(self,request):
        #TODO 회원가입
        email = request.data.get('email',None)
        nickname = request.data.get('nickname',None)
        name = request.data.get('name',None)
        password = request.data.get('password',None)
        
        if User.objects.filter(email=email).exists():
            return Response({'message': '이미 사용 중인 이메일입니다.'}, status=400)

        elif User.objects.filter(nickname=nickname).exists():
                    return Response({'message': '이미 사용 중인 닉네임입니다.'}, status=400)
            

        else:
            User.objects.create(email = email, 
                                nickname = nickname, 
                                username = name, 
                                password = make_password(password))

            return Response({'message': '회원가입 성공! 로그인해주세요.'},status=200)
        

#session을 통해 인증
# class Login(APIView):

#     def post(self, request):
#             email = request.data.get('email', None)
#             password = request.data.get('password', None)
            
#             user = authenticate(request, username=email, password=password)

#             if user is not None:
#                 request.session['email'] = email
#                 return Response(status=200)
#             else:
#                 return Response(status=400, data=dict(message="입력하신 아이디가 존재하지 않거나 패스워드가 일치하지 않습니다."))

#token통한 인증
class Login(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # 인증 성공 시 토큰 생성
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response(status=400, data=dict(message="입력하신 아이디가 존재하지 않거나 패스워드가 일치하지 않습니다."))

# 로그아웃 세션삭제
class Logout(APIView):
    def post(self,request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message': '로그아웃되었습니다.'}, status=200)


# 비밀번호 분실 시 이메일을 통한 비밀번호 재설정 가능. 비밀번호 변경 템플릿, 변경 후 로그인페이지로 리다이렉팅 필요
class ResetPassword(APIView):
    # def get(self, request):
    #     return render(request, "user/reset_password.html")

    def post(self, request):
        email = request.data.get('email')
        user = get_user_model().objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"{request.scheme}://{request.get_host()}/user/reset_password/{uid}/{token}/"

            # Send reset email
            email_subject = '비밀번호 재설정'
            email_message = render_to_string('user/reset_password_email.html', {
                'user': user,
                'reset_link': reset_link,
            })
            send_mail(email_subject, email_message, 'capturethekite@gmail.com', [user.email],html_message=email_message)

            messages.success(request, '비밀번호 재설정 이메일이 전송되었습니다.')
        else:
            messages.error(request, '해당 이메일을 사용하는 계정을 찾을 수 없습니다.')

        return Response({'message': '이메일이 전송되었습니다.'})
    

#유저 프로필 정보(닉네임, 이메일, 분야별 점수들)
class UserProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        #밑에2줄 확인용임 이따 지워
        session_key = request.session.session_key
        print("Session Key:", session_key, user)

        # 사용자의 프로필 정보 및 점수 정보를 가져오는 로직
        user_profile_serializer = UserProfileSerializer(user)
        user_score = UserScore.objects.get(user=user)
        user_score_serializer = UserScoreSerializer(user_score)

        profile_data = {
            'profile': user_profile_serializer.data,
            'scores': user_score_serializer.data,
        }

        return Response(profile_data, status=200)
        #return render(request, 'problem/main.html', context=profile_data)