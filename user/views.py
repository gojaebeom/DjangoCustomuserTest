from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'home.html')


# GET : 로그인 페이지 / POST : 로그인 요청
def login(request):
    if request.user.is_authenticated:
        print(request.user)
        print('잘못된 접근!!')
        return render(request, 'home.html', context={'message': '비정상적인 접근입니다'})

    # POST : 로그인 요청 처리
    if request.POST:
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        email = request.POST['email']
        password = request.POST['password']


        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, email=email, password=password)
        print(user)
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'login false'})

    # GET : 로그인 페이지 응답
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def join(request):
    if request.POST:
        print('요청받음 !')
        # 해당 User 모델은 장고에서 기본으로 제공해준다 ..
        CustomUser.objects.create_user(email=request.POST['email'], password=request.POST['password'])
        return redirect('/')
    
    return render(request, 'join.html')


from django.shortcuts import redirect 
import urllib 

    
# access token 요청
def kakao_callback(request):                                                                  
    params = urllib.parse.urlencode(request.GET)                                      
    return redirect(f'http://127.0.0.1:8000/account/login/kakao/callback?{params}')   
