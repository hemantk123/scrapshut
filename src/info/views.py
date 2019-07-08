from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import ProductForm

from .models import personal_info

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout


# Create your views here.

#home page   
def home_view(request,*args,**kwargs):
        return render(request,"base.html",{})

#form

@login_required
def product_view(request):
        if request.method == "POST":
                try:
                except personal_info.DoesNotExist:nfo.objects.get(user=request.info_instance = personal_info(user=request.user)
                form = ProductForm(request.POST or None, request.FILES, instance
                if form.is_valid():
                        obj = form.save(commit = False)
                        obj.user = request.user
                        obj.save()
                        return redirect('/profile')
        else:
       		 return render(request,"form_create.html",{'form':form})


def user_signup(request):
        if request.method == "POST":
                form = UserCreationForm(request.POST or None)
                if form.is_valid():
                        user = form.save()
                        login(request,user)
                        return redirect('/create')
        else:   
		form = UserCreationForm()
 	return render(request,'signup.html',{'form':form})



def user_login(request):
        if request.method == 'POST':
                form = AuthenticationForm(data=request.POST or None)
                if form.is_valid():
                        login(request,user)r()
                        return redirect('/profile')
        else: 
		  form = UserCreationForm()
                       AuthenticationForm()
        return render(request,'login.html',{'form':form})

@login_required
def profile_view(request):
        info_instance = personal_info.objects.get(user= request.user)
        context 'obj' : info_instance
        }
        return render(request,"profile.html",context)


def user_logout(request):
    logout(request)
    return redirect('/login')
    return render(request,'logout.html')
