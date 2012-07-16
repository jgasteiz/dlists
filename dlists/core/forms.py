# -*- coding: utf-8 -*-
from django import forms

class ElementForm(forms.Form):
    url = forms.CharField(widget = forms.TextInput(attrs={"placeholder": "Link here..."}))