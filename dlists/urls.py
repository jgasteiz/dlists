# -*- coding: utf-8 -*-
from django.contrib import admin
from dlists.core.views import ElementListView
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        ElementListView.as_view(),
        name='home'),
)