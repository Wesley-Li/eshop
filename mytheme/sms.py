#!/usr/bin/env python
#coding: gbk

import urllib
import urllib2
import random

sms_server = 'http://gbk.sms.webchinese.cn'
sms_uid = 'nipen2'
sms_key = '6f6a38d98fcb43fcace6'
sms_template = "您的验证码是{0},在五分钟内有效. 如非本人操作, 请忽略本信息.[食上海]"

def genchll():
    lista = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.sample(lista,4))

def sendSMS(cellnum,captchanum):
    url = sms_server
    values = {'Uid' : sms_uid,
              'Key' : sms_key,
              'smsMob' : cellnum,
                  "smsText": sms_template.format(captchanum) }
    headers = { 'Content-Type' : "application/x-www-form-urlencoded;charset=gbk" }
    
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    return response.read()
    

if __name__ == "__main__":
    url = 'http://gbk.sms.webchinese.cn'
    values = {'Uid' : 'nipen',
              'Key' : 'aa2f3fc559a2cc98c584',
              'smsMob' : '13851929937',
                  "smsText":"test" }
    headers = { 'Content-Type' : "application/x-www-form-urlencoded;charset=gbk" }
    
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    print response.read()