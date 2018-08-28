from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,"index.html",{'temp':1212})


def login_account(request):
	user="sohailkhan.sk"
	pw="Manofbadtheme"
	usr=authenticate(username=user,password=pw)
	if usr:
		if usr.is_active:
			login(request,usr)
			return HttpResponse(usr.email)
		else:
			return HttpResponse("not active")
	else:
		return HttpResponse("no user exist")