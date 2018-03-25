#!/usr/bin/env python
#coding: utf-8

from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="WNI_SEARCH_PLACEHOLDER",
    label=_("Search form placeholder"),
    description=_("Placeholder for search form on web page, for Ads purpose"),
    editable=True,
    default=u"香蕉牛奶特价,只要10元",
)