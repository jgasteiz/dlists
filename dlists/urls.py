# -*- coding: utf-8 -*-
from django.contrib import admin
from dlists.core.views import (ElementListView, ElementCreate, ElementUpdate, 
    ElementDelete, UpdateWeights)
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        ElementListView.as_view(),
        name='home'),
    url(r'^create/',
        ElementCreate.as_view(),
        name='create'),
    url(r'^update/',
        ElementUpdate.as_view(),
        name='update'),
    url(r'delete/',
        ElementDelete.as_view(),
        name='delete'),
    url(r'_ajax/update_weights/',
        UpdateWeights.as_view(),
        name='update_weights')
)
