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
    if request.method=='POST':
        template_var.update({'testInput':request.POST.get('testInput')+'form url exam'})
        #return render(request, "MyExam/Ok.html", template_var)
        return HttpResponseRedirect(reverse("MyExam:getForm"))
    else:
        template_var.update({'testInput': '测试一表单'})

    template_var.update({"username":"jiangyong"})

    return render(request,"MyExam/exam.html",template_var)

def getForm(request):
    template_var = {}
    if request.method == 'POST':
        testInput = request.POST.get("testInput")
        template_var.update({'testInput':testInput})
    else:
        testInput = 'form Redirect'
        template_var.update({'testInput': testInput})
    return render(request,'MyExam/Ok.html',template_var)