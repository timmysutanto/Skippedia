from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "New Account Created: {username}")
            login(request,user)
            return redirect('mahasiswa:index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    form = UserCreationForm
    return render(request,'login/home.html',context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out :)")
    return redirect('login:register')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, "Login Succesful")
                return redirect("mahasiswa:index")
            else:
                messages.error(request,"Invalid username/password")
        else:
            messages.error(request,"Invalid username/password")

    form = AuthenticationForm()
    return render(request, 'login/masuk.html', {"form":form})