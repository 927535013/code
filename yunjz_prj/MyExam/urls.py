from django.conf.urls import patterns, include, url
from django.contrib import admin
from MyExam import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^exam',views.exam,name='exam'),
    url(r'^getForm',views.getForm,name='getForm'),
)