# import urllib.request
# import urllib.parse
# import ssl
# import json
#
# # 请求百度翻译
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url = "https://fanyi.baidu.com/sug"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
# }
#
# data = {
#     'kw': 'xiao'
# }
#
# # post请求必须要使用urlencode编码,然后使用encode编码为二进制
# data = urllib.parse.urlencode(data).encode("UTF-8")
#
# # 创建一个request对象
# request = urllib.request.Request(url=url, data= data, headers=headers)
# # open发起请求
# response = urllib.request.urlopen(request)
#
# content = response.read().decode("UTF-8")
# print(content)
#
# # 字符串转json
# jsonStr = json.loads(content)
# print(jsonStr)

# {"errno":0,"data":[{"k":"Xiao","v":"[\u4e2d\u533b]\u5c0f\u513f\u836f\u8bc1\u76f4\u8bc0"},{"k":"xiao","v":"[\u4e2d\u533b]\u5c0f\u513f\u81f3\u5b9d\u4e38"},{"k":"xiaonei","v":"\u6821\u5185"}]}
# {'errno': 0, 'data': [{'k': 'Xiao', 'v': '[中医]小儿药证直诀'}, {'k': 'xiao', 'v': '[中医]小儿至宝丸'}, {'k': 'xiaonei', 'v': '校内'}]}


# post请求反扒处理
import urllib.request
import urllib.parse
import ssl
import json

 # 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

data = {
    'from':'ast',
    'to':'zh',
    'query':'xiaos',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'743027.1029442',
    'token':'0e94ec313fc3a656fcc173c97f4e26d7',
    'domain':'common'
}

# post请求需要对data进行编码
data = urllib.parse.urlencode(data).encode("UTF-8")

# 将请求头拷贝,使用cookie和user-agent处理反扒
headers = {
    'Accept':'*/*',
    # 在做爬虫时,这个请求头不能加上
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':'133',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'PSTM=1650631397; BAIDUID=95F2551B1062E427EAFA78AE7EB2BBB8:FG=1; BIDUPSID=65C93A8B3F6446DEF1D9155966C6AB58; BDUSS=VBUZH5KczVMNFJCRHlKeFBBb35LfnFMNHhOWG1HYk5wVGhYMG1vflFiczRPb3RpSVFBQUFBJCQAAAAAAAAAAAEAAAC27aEWzOyyxTE5OTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADitY2I4rWNiV; BDUSS_BFESS=VBUZH5KczVMNFJCRHlKeFBBb35LfnFMNHhOWG1HYk5wVGhYMG1vflFiczRPb3RpSVFBQUFBJCQAAAAAAAAAAAEAAAC27aEWzOyyxTE5OTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADitY2I4rWNiV; BDSFRCVID=M4uOJexroG0lawvDt3IzuiPPj9EtRXoTDYLtOwXPsp3LGJLVgZjfEG0Pt8wIvcA-eBm1ogKKLmOTHp-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbkD_C-MfIvDqTrP-trf5DCShUFsaJKJB2Q-XPoO3KJSDITPQMOPyRIXWG5I26jiWbRM2MbgylRp8P3y0bb2DUA1y4vpKbjP0eTxoUJ2XMKVDq5mqfCWMR-ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5P0hxry2Dr2aI52B5r_5TrjDnCrDf7TXUI82h5y05OQab5aKpbI-lcKoCohhj5vyT8sXnORXx74QC6L3lI-0xKKSCbKbn5lLxL1Db3JyhLLamTJslFy2t3oepvoDPJc3Mv30-jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtbuJVC-XfIK3qbT9btk_bJK8Kxoe-n3-KK-XWJ52fhvI_p7_bf--DRQy-xOr2f3J2nTqLRTxLncVMUj2e-Txy5K_hUvDJn533gbRoj6maq7GbqQHQT3m-lQbbN3i-4jmfRrPWb3cWhRV8UbSKKcPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eGKJtj_jJJCs3t88KJjEe-Kk-PnVeP-EX-nZKRvHa2kjWnj5KhbMhpTu5trm0-T-QqONXPRn3N5rKl75yUJ5qKOsQU6d34-lMxj405OTbnbfa4QJ066qERClhPJvyUADXnO7bIrlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_2JDD2MCDr-R-_-4_tbh_X5-RLf2DJLl7F54nKDp0xh-Qb5x03DPrE-4cTLIL8K4b4yn7xsMTs5MnbWh8yKabr0MTrQDvzBJQN3KJmfKn6yJjjLDu8LxFD2-biW2JL2Mbd-T6P_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-TryjHL8qUK; BDSFRCVID_BFESS=M4uOJexroG0lawvDt3IzuiPPj9EtRXoTDYLtOwXPsp3LGJLVgZjfEG0Pt8wIvcA-eBm1ogKKLmOTHp-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbkD_C-MfIvDqTrP-trf5DCShUFsaJKJB2Q-XPoO3KJSDITPQMOPyRIXWG5I26jiWbRM2MbgylRp8P3y0bb2DUA1y4vpKbjP0eTxoUJ2XMKVDq5mqfCWMR-ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5P0hxry2Dr2aI52B5r_5TrjDnCrDf7TXUI82h5y05OQab5aKpbI-lcKoCohhj5vyT8sXnORXx74QC6L3lI-0xKKSCbKbn5lLxL1Db3JyhLLamTJslFy2t3oepvoDPJc3Mv30-jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtbuJVC-XfIK3qbT9btk_bJK8Kxoe-n3-KK-XWJ52fhvI_p7_bf--DRQy-xOr2f3J2nTqLRTxLncVMUj2e-Txy5K_hUvDJn533gbRoj6maq7GbqQHQT3m-lQbbN3i-4jmfRrPWb3cWhRV8UbSKKcPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eGKJtj_jJJCs3t88KJjEe-Kk-PnVeP-EX-nZKRvHa2kjWnj5KhbMhpTu5trm0-T-QqONXPRn3N5rKl75yUJ5qKOsQU6d34-lMxj405OTbnbfa4QJ066qERClhPJvyUADXnO7bIrlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_2JDD2MCDr-R-_-4_tbh_X5-RLf2DJLl7F54nKDp0xh-Qb5x03DPrE-4cTLIL8K4b4yn7xsMTs5MnbWh8yKabr0MTrQDvzBJQN3KJmfKn6yJjjLDu8LxFD2-biW2JL2Mbd-T6P_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-TryjHL8qUK; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; BAIDUID_BFESS=755CC370F1D4A137A040E0542EB99E80:FG=1; BA_HECTOR=2181ag0g012gag24ov1h8a0ba0r; H_PS_PSSID=36426_36367_34812_35915_36165_34584_35979_36055_36419_36235_26350_36447; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1652883826; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1652883826; ab_sr=1.0.1_NjI3ZGNlOGFlODg1NDc0YjFjNjExMjFiMGVhNTVkODBjODU0MWJhOWVlNGQxZjNkNjc1OGFiMjk0MTk2YzUxZmYyYjlmZGRhOTY4OTcwYmFjNDJlMGUwNDM4ODQ1ZTI4M2UzZDAyYzA2MmFhNzkzNGU5OTdiMzQzMGIwMzhkZjkzYjM4NWRhNTNlODg4YWQ3Njk5ZjExZThkZDNiZDYxYjJhYjgzNjM5YWY0Y2Y5NGJjZDcwZTY4ZWE4ZTE1OGQw',
    'Host':'fanyi.baidu.com',
    'Origin':'https://fanyi.baidu.com',
    'Referer':'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
# 创建request对象
request = urllib.request.Request(url= url,data= data,headers= headers)
response = urllib.request.urlopen(request)

content = response.read().decode("UTF-8")
print(content)

print(json.loads(content))

