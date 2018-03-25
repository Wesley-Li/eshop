#!/usr/bin/env python
#coding: utf-8
'''
Created on 2014年7月2日

@author: Arc
'''
#from django.conf.urls.defaults import *
from django.conf.urls import *
import views
urlpatterns = patterns('',
(r'^$', views.interface),                       
(r'^test/$', views.test),
(r'^goods/$', views.goods),
#(r'^blog/entries/$', views.entry_list),
(r'^paytest/$', views.paytest),
(r'^payback/$', views.payback),
url("^getusercode/$",views.getUserCode,name='usercode'),
url(r'^getjspayparam/$', views.getjspayparam,name='getjsparam'),
(r'^home/$', views.homepage),
)
