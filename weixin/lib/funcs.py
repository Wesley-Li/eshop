#!/usr/bin/env python
#coding: utf-8

import random
import xml.etree.ElementTree as ET

def createNoncestr(length = 32):
    """产生随机字符串，不长于32位"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    strs = []
    for x in range(length):
        strs.append(chars[random.randrange(0, len(chars))])
    return "".join(strs)

def arrayToXml(arr):
    """array转xml"""
    xml = ["<xml>"]
    for k, v in arr.iteritems():
        if v.isdigit():
            xml.append("<{0}>{1}</{0}>".format(k, v))
        else:
            xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
    xml.append("</xml>")
    return "".join(xml)

def xmlToArray(xml):
    """将xml转为array"""
    array_data = {}
    root = ET.fromstring(xml)
    for child in root:
        value = child.text
        array_data[child.tag] = value
    return array_data