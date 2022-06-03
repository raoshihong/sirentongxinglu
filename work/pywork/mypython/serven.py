# 使用userAgent模拟浏览器,解决反爬虫问题
import urllib.request
import ssl

# 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 如果没有设置user-agent则只会返回部分数据
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode("UTF-8"))



# url = "https://www.baidu.com"
# # 使用user-agent,这个信息可以直接通过浏览器的network请求中的header信息找到
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
# }
# # 使用Request
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode("UTF-8"))

