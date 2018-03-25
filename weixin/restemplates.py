#!/usr/bin/env python
#coding: utf-8

from xml.dom import minidom
from django.http import HttpResponse

def genPicTxtRes(fromuser,touser,createtime,items):
    """
    <item> 
    <Title><![CDATA[python微信]]></Title>  
    <Description><![CDATA[description1]]></Description> 
    <PicUrl><![CDATA[http://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/486px-Python_logo_and_wordmark.svg.png]]></PicUrl> 
    <Url><![CDATA[url]]></Url> 
    </item> 
    <item> 
    <Title><![CDATA[python微信qq群 287714361]]></Title> 
    <Description><![CDATA[description]]></Description> 
    <PicUrl><![CDATA[http://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/486px-Python_logo_and_wordmark.svg.png]]></PicUrl> 
    <Url><![CDATA[url]]></Url> 
    </item> 
    """
    response = HttpResponse()
    response['Content-Type']="application/xml"
    tp = '''<xml> 
            <ToUserName>'''+touser+'''</ToUserName> 
    <FromUserName>'''+fromuser+'''</FromUserName> 
    <CreateTime>'''+createtime+'''</CreateTime> 
    <MsgType><![CDATA[news]]></MsgType> 
    <ArticleCount>%s</ArticleCount> 
    <Articles> 
    %s
    </Articles> 
    </xml>'''
    tmp = ''
    for item in items:
        tmp = tmp + """
       <item> 
       <Title><![CDATA[%s]]></Title>  
       <Description><![CDATA[%s]]></Description> 
       <PicUrl><![CDATA[%s]]></PicUrl> 
       <Url><![CDATA[%s]]></Url> 
       </item> 
       """ % (item['title'],item['description'],item['picurl'],item['url']) 
    tp %= (len(items),tmp)
    return response(tp)