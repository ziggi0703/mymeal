# !/usr/bin/env python
from django.conf.urls import patterns, url

from decision_maker import views

__author__ = 'Michael Ziegler'


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
