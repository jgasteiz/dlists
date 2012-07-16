# -*- coding: utf-8 -*-
from datetime import date
from dlists.core.models import Element
from dlists.core.forms import ElementForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect

class ElementListView(ListView):
    """
    Main page. Loads all the elements, ordered by date
    """
    context_object_name = 'element_list'
    template_name = 'core/element_list.html'

    def get_queryset(self):
        return Element.objects.all()

    def post(self, request, *args, **kwargs):
        e = Element()
        form = ElementForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            e.url = cd['url']
            e.save()
        return HttpResponseRedirect("/")

    def get_context_data(self, **kwargs):
        context = super(ElementListView, self).get_context_data(**kwargs)
        context.update({
                "form": ElementForm()
            })
        return context