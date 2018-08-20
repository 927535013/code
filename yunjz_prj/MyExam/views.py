#coding=utf-8
#django package
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.core.urlresolvers import reverse

def exam(request):
    template_var = {}
    template_var.update({"username":"jiangyong"})
    return render(request,"MyExam/exam.html",template_var)