# -*- coding: utf-8 -*-
from datetime import date
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView, TemplateView