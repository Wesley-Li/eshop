#!/usr/bin/env python
#coding: utf-8

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
import json,hashlib,os,time
from xml.dom import minidom
from payapi import UnifiedOrder_pub,JsApi_pub

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse,resolve
import urllib2,uuid
from lib.funcs import createNoncestr,arrayToXml
from lib.globalconfigs import getjsapiticket,getJsconfigSign
from cartridge.shop.templatetags.shop_tags import _order_totals
from wnisettings import APPID
from mezzanine.conf import settings

debug_weixin=True

trade_no_map = {}

def test(request):
    tst_dict = {'shit':'shit','fuck':'fuck'}
    #return HttpResponse(json.dumps(tst_dict))
    return HttpResponse(reverse('weixin:usercode'))
    #return render_to_response('test.html')

def paytest(request):
    """
    tst_dict = {'pay':'pay','tester':'wni'}
    #neworder = UnifiedOrder_pub()
    api_pub = JsApi_pub()
    #url = api_pub.createOauthUrlForCode(reverse('usercode'))
    #urllib2.urlopen()
    noncestr=createNoncestr()
    jsapi_ticket= getjsapiticket()
    timestamp=int(time.time())
    url=request.path
    sign = getJsconfigSign({'noncestr':noncestr,'jsapi_ticket':jsapi_ticket,'timestamp':timestamp,'url':url})
    #return HttpResponse(json.dumps(tst_dict))
    """
    #return render_to_response('paytest.html')
    api_pub = JsApi_pub()
    url = api_pub.createOauthUrlForCode('http://efoodin.com'+reverse('weixin:usercode'))
    return HttpResponseRedirect(url)

def getUserCode(request):
    try:
        api_pub = JsApi_pub()
        api_pub.setCode(request.GET.get('code'))
        openid = api_pub.getOpenid() 
        request.session['openid']=openid
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('get user code exception:%s\n'%e)
    #add get instead of request.session['onekeycode']
    #when homepage change to network+ style, weixin onekey order error that no onekeycode in session
    #but pc is OK, guess due to cookie forbidden within weixin browser, not diginto yet, just workaround here        
    return HttpResponseRedirect('http://%s/shop/checkout/?keycode=%s' % (settings.SITE_DOMAIN,request.session.get('onekeycode',None)))
    #wni: below is for weixin pay test
    #return render_to_response('paytest.html')

def getUserCode_bak(request,trade_no):
    try:
        api_pub = JsApi_pub()
        api_pub.setCode(request.GET.get('code'))
        openid = api_pub.getOpenid() 
        neworder = UnifiedOrder_pub()
        #"out_trade_no", "body", "total_fee", "notify_url", "trade_type"
        #tmp_no = uuid.uuid4().get_hex()
        neworder.setParameter('out_trade_no',trade_no)
        neworder.setParameter('body',u'e食部落美食')
        neworder.setParameter('total_fee','1')
        neworder.setParameter('trade_type','JSAPI')
        neworder.setParameter('openid',openid)
        neworder.setParameter('notify_url','http://efoodin.com/weixin/payback')
        with open('/tmp/wni.log','a') as f:
            f.write('neworder params:%s\n'% str(neworder.parameters))
        ppid = neworder.getPrepayId()
        api_pub.setPrepayId(ppid)
        params = api_pub.getParameters()
        trade_no_map[trade_no] = params
        with open('/tmp/wni.log','a') as f:
            f.write('js pay param:%s\n'%str(params))
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('get user code exception:%s\n'%e)
    return HttpResponse(json.dumps(params))
    #return render_to_response('paytest.html',{'parameters':params})

def getjspayparam(request):
    try:
        api_pub = JsApi_pub()
        neworder = UnifiedOrder_pub()
        #"out_trade_no", "body", "total_fee", "notify_url", "trade_type"
        trade_no = uuid.uuid4().get_hex()
        neworder.setParameter('out_trade_no',trade_no)
        neworder.setParameter('body',u'e食部落美食')
        #wni: below is for weixin pay test
        #neworder.setParameter('total_fee','1')
        #neworder.setParameter('total_fee',str(request.session.order.total*100))
        #neworder.setParameter('total_fee',str(float(request.session['order']['total']*100)))
        #tmp_total = request.session['order'].get_tmp_total(request)
        
        order_vars = _order_totals({"request": request})
        #print order_vars["order_total"]
        #neworder.setParameter('total_fee',str(request.session['wni_wxpay_total']*100))
        neworder.setParameter('total_fee',str(int(order_vars['order_total']*100)))
        neworder.setParameter('trade_type','JSAPI')
        neworder.setParameter('openid',request.session['openid'])
        neworder.setParameter('notify_url','http://%s/weixin/payback'%settings.SITE_DOMAIN)
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('order part exception:%s\n'% str(e))
            f.write('request.order is:%s\n'% str(request.session['order']))
            f.write('request.cart is:%s\n'% str(request.session['cart']))
    with open('/tmp/wni.log','a') as f:
        f.write('neworder params:%s\n'% str(neworder.parameters))
    try:
        ppid = neworder.getPrepayId()
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('get prepayid exception:%s\n'% str(e))
    api_pub.setPrepayId(ppid)
    params = api_pub.getParameters()
    
    noncestr=createNoncestr()
    jsapi_ticket= getjsapiticket()
    timestamp=int(time.time())
    #url=request.build_absolute_uri()
    #url = 'http://efoodin.com/weixin/paytest/'
    #url = 'http://efoodin.com/weixin/getusercode/'
    url = request.GET.get('signurl',None)
    with open('/tmp/wni.log','a') as f:
        f.write('url used to sign is:%s\n'% str(url))
    sign = getJsconfigSign({'noncestr':noncestr,'jsapi_ticket':jsapi_ticket,'timestamp':timestamp,'url':url})
    #return HttpResponse(json.dumps(tst_dict))
    tmp_dict = {'appId':APPID, 
    'timestamp': timestamp, 
    'nonceStr': noncestr, 
    'signature': sign}
    tmp_dict['pay_params'] = json.loads(params)
    if debug_weixin:
        with open('/tmp/wni.log','a') as f:
            f.write('\nparams for ajax is:%s\n'% str(tmp_dict))
    return HttpResponse(json.dumps(tmp_dict))

def getjspayparam_bak2(request):
    api_pub = JsApi_pub()
    neworder = UnifiedOrder_pub()
    #"out_trade_no", "body", "total_fee", "notify_url", "trade_type"
    trade_no = uuid.uuid4().get_hex()
    neworder.setParameter('out_trade_no',trade_no)
    neworder.setParameter('body',u'e食部落美食')
    neworder.setParameter('total_fee','1')
    neworder.setParameter('trade_type','JSAPI')
    neworder.setParameter('openid',request.session['openid'])
    neworder.setParameter('notify_url','http://efoodin.com/weixin/payback')
    with open('/tmp/wni.log','a') as f:
        f.write('neworder params:%s\n'% str(neworder.parameters))
    ppid = neworder.getPrepayId()
    api_pub.setPrepayId(ppid)
    params = api_pub.getParameters()
    return HttpResponse(json.dumps(params))

def getjspayparam_bak(request):
    with open('/tmp/wni.log','a') as f:
        f.write('enter getjspayparam func\n')
    try:
        tmp_no = uuid.uuid4().get_hex()
        neworder = UnifiedOrder_pub()
        api_pub = JsApi_pub()
        #url = api_pub.createOauthUrlForCode(reverse('weixin:usercode',args=(tmp_no,),current_app=resolve(request.path).namespace))
        url = api_pub.createOauthUrlForCode('http://eason.happydiaosi.com/weixin/getusercode/%s' % tmp_no)
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('create for code url exception:%s\n' % e)
    with open('/tmp/wni.log','a') as f:
        f.write('for code url:'+url)
    try:    
        #urllib2.urlopen(url)
        return HttpResponseRedirect(url)
    except Exception,e:
        with open('/tmp/wni.log','a') as f:
            f.write('open code url exception:%s\n'%e)
    #with open('/tmp/wni.log','a') as f:
    #    f.write('for code url opened, wating for openid&payparam')
    #time.sleep(5)
    #return HttpResponse(trade_no_map[tmp_no])
def payback(request):
    return HttpResponse(arrayToXml({'return_code':'SUCCESS','return_msg':'OK'}))

def goods(request):
    return render_to_response('test3.html')

def homepage(request):
    return render_to_response('home.html')

def interface(request):
    
    if request.method == 'GET':
        #获取输入参数
        signature=request.GET.get('signature',None)
        timestamp=request.GET.get('timestamp',None)       
        nonce=request.GET.get('nonce',None)        
        echostr=request.GET.get('echostr',None)
        
        #自己的token
        token="DiaoSi1"
        
        if None in [signature,timestamp,nonce]:
            os.system('echo "%s %s %s" > /tmp/wni.txt' % (signature,timestamp,nonce))
            return HttpResponse('Invalid request params!')
        #字典序排序    
        lista=[token,timestamp,nonce]
        lista.sort()
        hashcode=hashlib.sha1(''.join(lista)).hexdigest()
        #hashcode=hashlib.sha1(''.join(lista))
        #map(res.update,lista)
        #hashcode=res.hexdigest()
        #sha1加密算法        
        #如果是来自微信的请求，则回复echostr
        os.system('echo %r > /tmp/wni.txt' % signature)
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('shit')
    elif request.method == 'POST':
        #str_xml = web.data() #获得post来的数据
        #xml = etree.fromstring(str_xml)#进行XML解析
        geted = request.raw_post_data
        #with open('rawpost','w') as f1:
        #    f1.write(geted)
        xmldoc = minidom.parseString(geted)
        msgType = xmldoc.getElementsByTagName('MsgType')[0].childNodes[0].nodeValue
        if msgType == 'text':
            #content=request.POST.get("Content",None)#获得用户所输入的内容
            content = xmldoc.getElementsByTagName('Content')[0].childNodes[0].nodeValue
            #msgType=request.POST.get("MsgType",None)
            
            #fromUser=request.POST.get("FromUserName",None)
            fromUser = xmldoc.getElementsByTagName('FromUserName')[0].childNodes[0].nodeValue
            #toUser=request.POST.get("ToUserName",None)
            toUser = xmldoc.getElementsByTagName('ToUserName')[0].childNodes[0].nodeValue
            with open('revxml','w') as f:
                f.write('echo %r %r %r %r > /tmp/revxml.txt' % (content,msgType,fromUser,toUser))
            #os.system('echo %r %r %r %r > /tmp/revxml.txt' % (content,msgType,fromUser,toUser))
            #return HttpResponse('shit')
            response = HttpResponse()
            response['Content-Type']="application/xml"
            """
            return HttpResponse(<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml> % (fromUser,toUser,int(time.time()),content))
            """
            return HttpResponse("""<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[transfer_customer_service]]></MsgType>
            </xml>""" % (fromUser,toUser,int(time.time())))
                    
            #return self.render.reply_text(fromUser,toUser,int(time.time()),u"我现在还在开发中，还没有什么功能，您刚才说的是："+content)
        elif msgType == 'event':
            pass