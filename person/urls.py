# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('person.views',
    url(r'[^/]+/(\d+)', 'person_details', name='person_details'),
)