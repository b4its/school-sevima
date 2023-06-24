from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm 
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import Profile
# authenticated function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .helpers import send_forget_password_mail

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("you're authenticated ")
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Proses registrasi anda telah berhasil, silahkan untuk login!')
                return redirect('customerlogin')

            else:
                messages.error(request,'Password kamu mungkin tidak sama atau password sesuai dengan username!')
                return redirect('register')
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def customerlogin (request):
    if request.user.is_authenticated:
        return HttpResponse("you're already login ")
    else:
        if request.method == 'post' or request.method == 'POST':
            username = request.POST.get('username')    
            password = request.POST.get('password')    
            customer = authenticate(request,username=username,password=password)
            if customer is not None:
                login(request,customer)
                messages.info(request,'Selamat Datang '+str(request.user)+'!')
                return redirect('index')
            else:
                messages.error(request,'Username atau password kamu salah!')
                return redirect('customerlogin')

    return render(request,'login.html')

@login_required
def logout_view(request):
	if request.method =="POST":
		logout(request)
		return redirect("customerlogin")
	return render(request, "logout.html")

def change_password(request, token):
    try:
        profile = Profile.objects.filter(token=token).first()
        if request.method == "POST":
            akun = User.objects.get(username=profile.user.username)
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                akun.set_password(password)
                akun.save()
                messages.success(request, 'Anda telah berhasil mengatur ulang password anda !')
                return redirect('customerlogin')
            else:
                messages.error(request, 'Mohon maaf tidak sesuai dengan sebelumnya !')
                

        context = {
            'user_id':profile.user.pk
        }
    except Profile.DoesNotExist:
        messages.error(request, 'Limit token anda sudah habis!')
        return redirect('lupa_password')

    return render(request, "change_password.html",context)

import uuid


def lupa_password(request):

        if request.method == "POST":
            username = request.POST.get('username')
            if not User.objects.filter(username = username).first():
                
                messages.error(request,'Username anda tidak ditemukan!')
                return redirect('lupa_password')
            else:
                pengguna = User.objects.get(username = username)
                token = str(uuid.uuid4())
                send_forget_password_mail(pengguna.email, token)
                tes = Profile.objects.get(user = pengguna)
                tes.token = token
                tes.save()
                messages.success(request,'Kodenya telah berhasil dikirim!')
                return redirect('lupa_password')
            


		
        
        return render(request, "lupa_password.html")