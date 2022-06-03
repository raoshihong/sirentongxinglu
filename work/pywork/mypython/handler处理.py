import urllib.request
import ssl

 # 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.dushu.com/"
request = urllib.request.Request(url = url)

# 创建handler
handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

# 请求
response = opener.open(request)

content = response.read().decode("UTF-8")

with open(file="1.html",mode="w") as fp:
    fp.write(content)