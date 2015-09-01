#coding=utf-8
#django package
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User  
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
def index(request):
    return render_to_response("accounts/index.html",)

def register(request):
    '''注册视图'''
    if request.method=="POST":
        #注册完毕 直接登陆
        return HttpResponseRedirect("/accounts/index")            
    return render_to_response("accounts/register.html",)

	
def login(request):
    '''登陆视图'''
    template_var={}    
    if request.method == 'POST':
        template_var={"error":"you must first register"}                 
    return render_to_response("accounts/login.html",template_var,)
    
	
def logout(request):
    return render_to_response('accounts/logout.html',)	
	
