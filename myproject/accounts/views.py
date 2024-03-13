from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .forms import UploadFileForm
import json
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import requests


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    # Erişim tokeni al
    client_id = 'u-s4t2ud-9ed26e8ac69f5716daf9a72c876ceadaef71860a128ef344d7cf8fcb4cac07ef'
    client_secret = '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'
    redirect_uri = 'https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-9ed26e8ac69f5716daf9a72c876ceadaef71860a128ef344d7cf8fcb4cac07ef&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fsuccess%2F&response_type=code'

    # 42 API ile doğrulama işlemi başlatma
    authorization_url = f'https://api.intra.42.fr/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(authorization_url)

def success_view(request):
    username = request.user.username  # Şu anki kullanıcının kullanıcı adını al
    return render(request, 'accounts/success.html', {'username': username})


def home_view(request):
    return HttpResponse('<h1>Ana Sayfa</h1>')

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_content = request.FILES['file'].read()
            try:
                users_data = json.loads(file_content.decode('utf-8'))

                for user_data in users_data:
                    # Django'nun kullanıcı oluşturma fonksiyonunu kullanarak yeni kullanıcıyı oluşturun.
                    user = User.objects.create_user(
                        username=user_data['name'], 
                        email=user_data['email'],
                        password=user_data['password']  # Parolaları burada belirtin
                    )
                    # Alternatif olarak, User modeli için 'set_password' fonksiyonunu da kullanabilirsiniz.
                    # user.set_password(user_data['password'])
                    # user.save()

                return HttpResponse("Kullanıcılar başarıyla eklendi.")
            except json.JSONDecodeError as e:
                return HttpResponse(f"JSON decode hatası: {e}", status=400)
            except Exception as e:
                return HttpResponse(f"Bir hata oluştu: {e}", status=400)
    else:
        form = UploadFileForm()
    return render(request, 'accounts/upload_file.html', {'form': form})


def list_users_view(request):
    users = User.objects.all()  # Tüm kullanıcıları çek
    return render(request, 'accounts/list_users.html', {'users': users})

def callback_42(request):
    # 42 API'den gelen doğrulama kodunu al
    authorization_code = request.GET.get('code', None)

    if authorization_code:
        # 42 API'den kullanıcı bilgilerini almak için token talep etme
        token_url = 'https://api.intra.42.fr/oauth/token'
        client_id = 'u-s4t2ud-9ed26e8ac69f5716daf9a72c876ceadaef71860a128ef344d7cf8fcb4cac07ef'
        client_secret = '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'
        redirect_uri = 'https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-9ed26e8ac69f5716daf9a72c876ceadaef71860a128ef344d7cf8fcb4cac07ef&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fsuccess%2F&response_type=code'  # 42 API uygulama ayarlarında belirttiğiniz URI

        payload = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
        }

        response = requests.post(token_url, data=payload)
        token_data = response.json()

        if 'access_token' in token_data:
            # 42 API'den kullanıcı bilgilerini al
            user_url = 'https://api.intra.42.fr/v2/me'
            headers = {'Authorization': f'Bearer {token_data["access_token"]}'}
            user_response = requests.get(user_url, headers=headers)
            user_data = user_response.json()

            # Django'da kullanıcı oluştur veya giriş yap
            if user_data.get('id'):
                username = user_data['login']
                # Eğer Django'da böyle bir kullanıcı varsa, onu getir, yoksa oluştur
                user, created = User.objects.get_or_create(username=username)
                login(request, user)
                return redirect('success')

    return redirect('login')


def new_funcation(request):
    code = request.GET.get('code')

    if code:
        print("request    asdasdasd       ", request)

    else:
        return render(request, 'accounts/error_login.html')

    return success_view(request)
