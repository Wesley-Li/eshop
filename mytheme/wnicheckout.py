#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.template.loader import get_template, TemplateDoesNotExist
from mezzanine.accounts import get_profile_for_user, ProfileNotConfigured

from mezzanine.conf import settings
from mezzanine.utils.email import send_mail_template

from cartridge.shop.models import Order
from cartridge.shop.utils import set_shipping, set_tax, sign


class CheckoutError(Exception):
    """
    Should be raised in billing/shipping and payment handlers for
    cases such as an invalid shipping address or an unsuccessful
    payment.
    """
    pass


def wni_billship_handler(request, order_form):
    """
    Default billing/shipping handler - called when the first step in
    the checkout process with billing/shipping address fields is
    submitted. Implement your own and specify the path to import it
    from via the setting ``SHOP_HANDLER_BILLING_SHIPPING``.
    This function will typically contain any shipping calculation
    where the shipping amount can then be set using the function
    ``cartridge.shop.utils.set_shipping``. The Cart object is also
    accessible via ``request.cart``
    """
    if not request.session.get("free_shipping"):
        settings.use_editable()
        if request.cart.total_price() > settings.FREE_SHIPPING_TOTAL:
            set_shipping(request, "Free shipping", 0)
            return 
        set_shipping(request, _("Flat rate shipping"),
                     settings.SHOP_DEFAULT_SHIPPING_VALUE)
