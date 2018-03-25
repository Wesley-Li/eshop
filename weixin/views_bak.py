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
from lib.funcs import createNoncestr
from lib.globalconfigs import getjsapiticket,getJsconfigSign
from wnisettings import APPID

trade_no_map = {}

def test(request):
    tst_dict = {'shit':'shit','fuck':'fuck'}
    #return HttpResponse(json.dumps(tst_dict))
    return render_to_response('test.html')

def paytest(request):
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
    return render_to_response('paytest.html',{'appId':APPID, 
    'timestamp': timestamp, 
    'nonceStr': noncestr, 
    'signature': sign})

def getUserCode(request,trade_no):
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

def goods(request):
    return render_to_response('test3.html')

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