
# import urllib.request
# import ssl
#
#  # 跳过证书验证
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url = "https://www.jd.com/"
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# content = response.read().decode("UTF-8")
# print(content)

# 直接上面到方式是获取不到京东描述页面数据到,需要使用selenium模拟浏览器才能获取到

# 引入驱动
from selenium import webdriver

# 我们下载到selenium chrome驱动包路径
path = "chromedriver"
# 获取浏览器对象
brower = webdriver.Chrome(path)

url = "https://www.jd.com/"
# 打开浏览器发起请求
brower.get(url)

# 通过浏览器对象获取页面源码
content = brower.page_source
print(content)
