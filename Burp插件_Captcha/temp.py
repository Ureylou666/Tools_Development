#!/usr/bin/env python
import base64
import json
import re
import urllib
import ssl      

url = 'https://im1.csc.ikea.cn/v10/common/imgVerifyCode'
request = urllib2.Request(url,data="")
response = urllib2.urlopen(request).read()
stat1 = json.loads(response)
codeId = stat1["entity"]["codeId"]
xp_captcha_url = xp_captcha_url + codeId
