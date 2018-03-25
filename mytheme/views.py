# Create your views here.
#coding: utf-8

from django.contrib.auth.decorators import login_required
from cartridge.shop.models import DiscountCode
from cartridge.shop.models import Order
from mezzanine.utils.views import render, set_cookie, paginate
from mezzanine.conf import settings
from sms import sendSMS,genchll
from settings import cell_captcha_map
from settings import logger
from time import time
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext


@login_required
def my_discount(request, template="shop/my_discounts.html"):
    """
    Display a list of the currently logged-in user's past orders.
    """
    all_orders = (DiscountCode.objects.filter(active=1)
                  .filter(validusers__id=request.user.id))
    orders = paginate(all_orders.order_by('-id'),
                      request.GET.get("page", 1),
                      settings.SHOP_PER_PAGE_CATEGORY,
                      settings.MAX_PAGING_LINKS)
    context = {"orders": orders}
    return render(request, template, context)


def my_discount_ajax(request,template="shop/cart_my_discount.html"):
    """
    Display a list of the currently logged-in user's past orders.
    """
    if request.user.is_authenticated():
        #all_orders = (DiscountCode.objects.filter(active=1)
                      #.filter(validusers__id=request.user.id))
        #discount_codes = DiscountCode.objects.active().filter(validusers__id=request.user.id).values("title","code","valid_to","uses_remaining","description")
        discount_codes = DiscountCode.objects.active().filter(validusers__id=request.user.id)
        #return HttpResponse(json.dumps(discount_codes)) 
        #context = {"orders": discount_codes}
        #return render(request, template, context)
        return render_to_response(template,{"orders": discount_codes},context_instance=RequestContext(request))
    else:
        return HttpResponse("<div>请先<a href='/accounts/login/?next=/shop/cart/'>登录!</a></div>")

from django.shortcuts import render_to_response
def wni_test(request,template="shop/test.html"):
    return render_to_response(template)

def wxwrap(request,template="wxwrap.html"):
    return render_to_response(template,context_instance=RequestContext(request))

from cartridge.shop.templatetags.shop_tags import _order_totals
def orderTotal(request):
    order_vars = _order_totals({"request": request})
    return HttpResponse(order_vars["order_total"])


def pushSMS(request):
    if request.method == "POST":
        cellnum = request.POST.get('cn',None)
        tp = request.POST.get('tp',None)
        if None in (cellnum,tp):
            #raise Exception("cn or ca is None from request!")
            return HttpResponse(-1)
        if int(tp)==0:
            chll = genchll()
            ret = sendSMS(cellnum,chll)
            #ret = 0
            if ret <= 0:
                logger.log(40,"sending sms to %s failed ret code %s" % (cellnum,ret))
                return HttpResponse(ret)
            if cellnum in cell_captcha_map:
                cell_captcha_map[cellnum].append((chll,int(time())))
            else:
                cell_captcha_map[cellnum] = [(chll,int(time()))]
            return HttpResponse(1)
        elif int(tp)==1:
            #cell_captcha_map["13270806549"] = [("1234",time()),]
            chargekey = request.POST.get('ca',None)
            if chargekey is None:
                return HttpResponse(990)
            if cellnum not in cell_captcha_map:
                return HttpResponse(991)
            for cap,timestamp in cell_captcha_map[cellnum]:
                if int(time())-timestamp>300:
                    cell_captcha_map[cellnum].remove((cap,timestamp))
                else:
                    if cap==chargekey:
                        return HttpResponse(999)
            return HttpResponse(992)

def verifySMS(request):
    if request.method == "POST":
        cellnum = request.POST.get('cn',None)
        captchanum = request.POST.get('ca',None)  

                          
def checkcellfirst(request):
    #wni: add below line to disable sms verify
    return HttpResponse(0)
    if request.method == "POST":
        cellnum = request.POST.get('cn')
        counter =  Order.objects.filter(billing_detail_phone__exact=cellnum.strip()).count()
        if counter > 0:
            return HttpResponse(0)
        else:
            chllnum = genchll()
            ret = sendSMS(cellnum,chllnum)
            #ret = 0
            if ret <= 0:
                logger.log(40,"sending sms to %s failed ret code %s" % (cellnum,ret))
            if cellnum in cell_captcha_map:
                cell_captcha_map[cellnum].append((chllnum,int(time())))
            else:
                cell_captcha_map[cellnum] = [(chllnum,int(time()))]
            return HttpResponse(1)
        
def cartCount(request):
    return HttpResponse(request.cart.cartcounter())        

def checkuserexist(request):
    if request.method == "POST":
        cellnum = request.POST.get('em')
        counter =  User.objects.filter(email__iexact=cellnum.strip()).count()
        if counter > 0:
            return HttpResponse(1)
        else:
            return HttpResponse(0)        

def getOneKeyCode(request):
    request.session['onekey']='33333'
    return HttpResponse('33333')