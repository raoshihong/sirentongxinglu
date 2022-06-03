# # 使用quote编码
# # https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# import urllib.request
# import urllib.parse
# import ssl
#
# # 跳过证书验证
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # get请求参数需要使用url编码转化为unicode编码
# wd = urllib.parse.quote("周杰伦")
# url = "https://www.baidu.com/s?wd="+wd
# print(url)
# # 使用user-agent,这个信息可以直接通过浏览器的network请求中的header信息找到
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
# }
# # 使用Request
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode("UTF-8"))





# # 使用urlencode编码
# # https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# import urllib.request
# import urllib.parse
# import ssl
#
# # 跳过证书验证
# ssl._create_default_https_context = ssl._create_unverified_context
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '台湾'
# }
# # get请求参数需要使用url编码转化为unicode编码
# url = "https://www.baidu.com/s?"+urllib.parse.urlencode(data)
# print(url)
# # 使用user-agent,这个信息可以直接通过浏览器的network请求中的header信息找到
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
# }
# # 使用Request
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode("UTF-8"))
