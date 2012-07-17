# -*- coding: utf-8 -*-
from datetime import date
from dlists.core.models import Element
from dlists.core.forms import ElementForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


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

class ElementCreate(CreateView):
    model = Element

class ElementUpdate(UpdateView):
    model = Element

class ElementDelete(DeleteView):
    model = Element