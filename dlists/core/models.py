# -*- coding: utf-8 -*-
from urllib2 import urlopen
from django.db import models
from datetime import datetime
from django.utils.timezone import utc
from BeautifulSoup import BeautifulSoup
from dlists.core.forms import ElementForm
from django.utils.translation import ugettext_lazy as __


class Element(models.Model):
    """
    Stores a single blog entry

    """
    title = models.CharField(__('Title'), blank=True, max_length=240)
    url = models.URLField(__('URL'), blank=False, max_length=512)
    created = models.DateTimeField(__('Creation Date'), 
        default=datetime.utcnow().replace(tzinfo=utc))
    weight = models.IntegerField(__('Weight'), default=0)

    class Meta:
        ordering = ('weight','-created',)
        verbose_name, verbose_name_plural = 'Element', 'Elements'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            soup = BeautifulSoup(urlopen(self.url))
            self.title = unicode(soup.title.string)
        super(Element, self).save(*args, **kwargs)