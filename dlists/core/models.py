# -*- coding: utf-8 -*-
from lxml import html
from django.db import models
from datetime import datetime
from dlists.core.forms import ElementForm
from django.utils.translation import ugettext_lazy as __


class Element(models.Model):
    """
    Stores a single blog entry

    """
    title = models.CharField(__('Title'), blank=True, max_length=240)
    url = models.URLField(__('URL'), blank=False, max_length=512)
    updated = models.DateTimeField(__('Update Date'), auto_now_add=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name, verbose_name_plural = 'Element', 'Elements'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        if not self.title:
            t = html.parse(self.url)
            self.title = t.find(".//title").text
        super(Element, self).save(*args, **kwargs)