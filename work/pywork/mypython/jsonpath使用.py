import json
import urllib.request

import jsonpath

import ssl

 # 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1653129432312_129&jsoncallback=jsonp130&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cItyaction.json?activItyId&_KsTS=1653129432312_129&jsoncallback=jsonp130&action=cItyaction&n_s=new&event_submit_doGetAllregion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ZH-cn,zh;q=0.9',
    'cookie': 't=a7b78395eb5c78ac87bc94b97ea5da23; cookie2=164e9ffd158b1973ec06c09cdfd020ab; v=0; _tb_token_=86eb3f6fe3b7; cnA=nGn3Gh01/VmCAD+YczGW4SBk; xlly_s=1; tfstk=cOUcb3JoPy9bjCMuaZgF5PHatyJDaROrhryBZSaSYhc-DdasgsV94HuD0gdldt-1.; L=EBPVMUV7LxL2xPQhBofzourzA77TBirAguPzAnBMIOcpOuFH5YFpW6fT68tMCngvHSbBR3-4a-mBBeyBch4sjqj4axoM42Mmn; iSG=BDk51mSRF6bHMIM0c7nZ9YCDSKmTRi34ij5vcltUrmdf4ll0o5FwyPW8ZOyU2sUw',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '" NOt a;brand";v="99", "chromium";v="101", "googLe chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"MAcOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'mozilla/5.0 (macintosH; intEl MAC OS X 10_15_7) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/101.0.4951.64 safari/537.36',
    'x-requested-with': 'XmlhTtprequest',
}

request = urllib.request.Request(url = url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("UTF-8")

content = content.replace('jsonp130(','')
content = content[0:len(content)-2]

jsonObj = json.loads(content)

regionName = jsonpath.jsonpath(jsonObj,"$.returnValue[*]..regionName")
print(regionName)

