# -*- coding: utf-8 -*-
from django.contrib import admin
from dlists.core.models import Element


class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'weight', 'created')


admin.site.register(Element, ElementAdmin)