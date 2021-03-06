#!/usr/bin/env python
#coding:gbk
from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
import base64
import json
import re
import urllib2
import ssl

host = ('127.0.0.1', 9999)

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        callbacks.setExtensionName("free_xp_CAPTCHA")

    def getGeneratorName(self):
        return "xp_CAPTCHA"

    def createNewInstance(self, attack):
        return xp_CAPTCHA(attack)

class xp_CAPTCHA(IIntruderPayloadGenerator):
    def __init__(self, attack):
        tem = "".join(chr(abs(x)) for x in attack.getRequestTemplate()) 
        cookie = re.findall("Cookie: (.+?)\r\n", tem)[0]
        xp_CAPTCHA = re.findall("xiapao:(.+?)\r\n", tem)[0]
        ssl._create_default_https_context = ssl._create_unverified_context 
        print xp_CAPTCHA+'\n'
        print 'cookie:' + cookie+'\n'
        self.xp_CAPTCHA = xp_CAPTCHA
        self.cookie = cookie
        self.max = 1
        self.num = 0
        self.attack = attack

    def hasMorePayloads(self):
        if self.num == self.max:
            return False
        else:
            return True

    def getNextPayload(self, payload):
        xp_CAPTCHA_url = self.xp_CAPTCHA
        
        request = urllib2.Request(xp_CAPTCHA_url,data='test=123')
        response = urllib2.urlopen(request).read()
        codeId = json.loads(response)["entity"]["codeId"]
        xp_CAPTCHA_url = xp_CAPTCHA_url + "?codeId="+codeId

        print xp_CAPTCHA_url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36","Cookie":self.cookie}
        request = urllib2.Request(xp_CAPTCHA_url,headers=headers)
        CAPTCHA = urllib2.urlopen(request)
        CAPTCHA_base64 = base64.b64encode(CAPTCHA.read())

        request = urllib2.Request('http://%s:%s/base64'%host, 'base64='+CAPTCHA_base64)
        response = urllib2.urlopen(request).read()
        print(response)
        value2 = codeId + '%22,%22codeValue%22:%22'+ response
        return value2

    def reset(self):
        self.num = 0
        return