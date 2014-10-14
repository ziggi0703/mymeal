# !/usr/bin/env python
from django.conf.urls import patterns, url

from decision_maker import views

__author__ = 'Michael Ziegler'


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^vote_form', views.vote_form, name='vote_form'),
    url(r'^(?P<date>\d+)/vote$', views.vote, name='vote'),
    url(r'^(?P<pk>\d+)/user_result', views.UserResultView.as_view(), name='user_result'))