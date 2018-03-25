#!/usr/bin/env python
#coding: utf-8

import urllib2
from ..wnisettings import APPID,APPSECRET,ACCESSTOKENTTL
import time
from logger import pub_logger
import json
import hashlib

wx_dy_configs = {}

def getaccesstoken():
    tmp = int(time.time())
    if 'accesstoken' in wx_dy_configs and tmp-wx_dy_configs['accesstoken']['ttl']<ACCESSTOKENTTL:
        return wx_dy_configs['accesstoken']['value']
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (APPID,APPSECRET)
    res = json.loads(urllib2.urlopen(url).read())
    if 'access_token' in res:
        tmp_dict = {}
        tmp_dict['ttl'] = int(time.time())
        tmp_dict['value'] = res['access_token']
        wx_dy_configs['accesstoken']=tmp_dict
        return res['access_token']
        
    else:
        pub_logger.log(40,'Get accesstoken failed:%s'%res[errmsg])
    
def getjsapiticket():
    tmp = int(time.time())
    if 'jsapiticket' in wx_dy_configs and tmp-wx_dy_configs['jsapiticket']['ttl']<ACCESSTOKENTTL:
        return wx_dy_configs['jsapiticket']['value']
    accesstoken=getaccesstoken()
    if accesstoken is None:
        pub_logger.log(40,'Get jsapiticket failed due to none accesstoken')
        return
    url= 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi' % accesstoken
    res = json.loads(urllib2.urlopen(url).read())
    if 'ticket' in res:
        tmp_dict = {}
        tmp_dict['ttl'] = int(time.time())
        tmp_dict['value'] = res['ticket']
        wx_dy_configs['jsapiticket'] = tmp_dict
        return res['ticket']
    else:
        pub_logger.log(40,'Get accesstoken failed:%s'%res[errmsg])
        

def formatDict(paraMap, urlencode):
        """格式化参数，签名过程需要使用"""
        slist = sorted(paraMap)
        buff = []
        for k in slist:
            v = quote(paraMap[k]) if urlencode else paraMap[k]
            buff.append("{0}={1}".format(k, v))

        return "&".join(buff)

def getJsconfigSign(obj):
        """生成签名"""
        #签名步骤一：按字典序排序参数,formatBizQueryParaMap已做
        String = formatDict(obj, False)
        #签名步骤二：在string后加入KEY
        #String = "{0}&key={1}".format(String,WxPayConf_pub.KEY)
        #签名步骤三：MD5加密
        String = hashlib.sha1(String).hexdigest()
        #签名步骤四：所有字符转为大写
        #result_ = String.upper()
        return String