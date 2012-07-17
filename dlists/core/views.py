# -*- coding: utf-8 -*-
from json import loads
from datetime import date
from dlists.core.models import Element
from dlists.core.forms import ElementForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, View


class ElementListView(ListView):
    """
    Main page. Loads all the elements, ordered by date
    """
    context_object_name = 'element_list'
    template_name = 'core/element_list.html'

    def get_queryset(self):
        return Element.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ElementListView, self).get_context_data(**kwargs)
        context.update({
                "form": ElementForm()
            })
        return context


class ElementCreate(View):
    def post(self, request, *args, **kwargs):
        if request.POST['url']:
            Element(url=request.POST['url']).save()
        return HttpResponseRedirect('/')


class ElementUpdate(View):
    def post(self, request, *args, **kwargs):
        if request.POST['pk'] and request.POST['title']:
            e = Element.objects.filter(pk=request.POST['pk'])[0]
            e.title = request.POST['title']
            e.save()
        return HttpResponseRedirect('/')


class ElementDelete(View):
    def post(self, request, *args, **kwargs):
        if request.POST['pk']:
            Element.objects.filter(pk=request.POST['pk']).delete()
        return HttpResponseRedirect('/')


class UpdateWeights(View):
    def post(self, request, *args, **kwargs):
        if request.POST['ids']:
            ids = loads(request.POST['ids'])
            i = 0
            for id in ids:
                Element.objects.filter(pk=id).update(weight=i)
                i = i + 1
        return HttpResponseRedirect('/')

