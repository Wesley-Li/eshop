#!/usr/bin/env python
#coding: utf-8

import urllib,urllib2,sys

import json
from wnisettings import appid,secret
from lib.logger import pub_logger

 
class MenuManager(object):
    
    def __init__(self):
        self.accessUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appid,secret)
        self.delMenuUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=" 
        self.createUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token="
        self.getMenuUri="https://api.weixin.qq.com/cgi-bin/menu/get?access_token=" 
    
    def getAccessToken(self): 
        f = urllib2.urlopen(self.accessUrl)
        accessT = f.read().decode("utf-8") 
        jsonT = json.loads(accessT)
        if 'access_token' not in jsonT:
            pub_logger.log(40,'No key access_token found at %s' % jsonT)
            raise Exception('No key access_token found!')
        return jsonT["access_token"]
  
    def delMenu(self, accessToken):  
        html = urllib2.urlopen(self.delMenuUrl + accessToken)
        result = json.loads(html.read().decode("utf-8")) 
        if 'errcode' not in result or result['errcode'] != 0:
            pub_logger.log(40,'Deleting menu failed detected from %s' % result)
            raise Exception('Deleting menu failed!')
        #return result["errcode"]
    
  
    def createMenu_succ(self, accessToken):
        menu = """
        {
                 "button":[ 
                     {   
          "type":"click",
          "name":"今日歌曲",
          "key":"V1001_TODAY_MUSIC"
      },
      { 
           "type":"view",
           "name":"歌手简介",
           "url":"http://www.baidu.com/"
      },
      { 
           "name":"菜单",
           "sub_button":[ 
            {"type":"click","name":"视频","key":"V1001_HELLO_WORLD"},{"type":"click","name":"赞一下我们","key":"V1001_GOOD"}]}]}
    """
        reload(sys)
        #cf=ConfigParser.ConfigParser()
        defaultcoding = sys.getdefaultencoding()
        #cf.readfp(codecs.open('./env2.bc','r','utf-8-sig'))
        sys.setdefaultencoding('utf-8')
        #cf.write(codecs.open('./env2.bc','w','utf-8-sig'))

        print menu
        
        req = urllib2.Request(self.createUrl + accessToken, menu)
        html = urllib2.urlopen(req)
        #html = urllib2.urlopen(self.createUrl + accessToken, urllib.urlencode(menu))
        #html = urllib2.urlopen(self.createUrl + accessToken, menu.encode("utf-8"))
        result = json.loads(html.read().decode("utf-8"))
        sys.setdefaultencoding(defaultcoding)
        if 'errcode' not in result or result['errcode'] != 0:
            pub_logger.log(40,'Creating menu failed detected from %s' % result)
            raise Exception('Creating menu failed!') 
        #return result["errcode"]
        
    def createMenu(self, accessToken):
        menu = {
                 "button":[ 
                     {   
          "type":"click",
          "name":"今日歌曲",
          "key":"V1001_TODAY_MUSIC"
      },
      { 
           "type":"view",
           "name":"歌手简介",
           "url":"http://www.baidu.com/"
      },
      { 
           "name":"菜单",
           "sub_button":[ 
            {"type":"click","name":"视频","key":"V1001_HELLO_WORLD"},{"type":"click","name":"赞一下我们","key":"V1001_GOOD"}]}]}
    
        reload(sys)
        #cf=ConfigParser.ConfigParser()
        defaultcoding = sys.getdefaultencoding()
        #cf.readfp(codecs.open('./env2.bc','r','utf-8-sig'))
        sys.setdefaultencoding('utf-8')
        #cf.write(codecs.open('./env2.bc','w','utf-8-sig'))

        #print menu
        tmp = json.dumps(menu,ensure_ascii=False)
        #print tmp
        req = urllib2.Request(self.createUrl + accessToken, tmp)
        html = urllib2.urlopen(req)
        #html = urllib2.urlopen(self.createUrl + accessToken, urllib.urlencode(menu))
        #html = urllib2.urlopen(self.createUrl + accessToken, menu.encode("utf-8"))
        result = json.loads(html.read().decode("utf-8"))
        sys.setdefaultencoding(defaultcoding)
        if 'errcode' not in result or result['errcode'] != 0:
            pub_logger.log(40,'Creating menu failed detected from %s' % result)
            raise Exception('Creating menu failed!') 
        #return result["errcode"]
  
    def getMenu(self):
        html = urllib2.urlopen(self.getMenuUri + accessToken)
        pub_logger.log(10,html.read().decode("utf-8"))  
  
  
if __name__ == "__main__":
  
    wx = MenuManager()
    accessToken = wx.getAccessToken() 
    pub_logger.log(10,'access:%s' % accessToken)
    #wx.delMenu(accessToken)
    wx.createMenu(accessToken)  
    #wx.getMenu()
  
        
  