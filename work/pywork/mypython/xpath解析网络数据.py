import urllib.request

from lxml import etree

url = "http://www.baidu.com"

request = urllib.request.Request(url=url)

response = urllib.request.urlopen(request)

content = response.read().decode("UTF-8")

# 使用xpath解析网络资源
tree = etree.HTML(content)

value = tree.xpath('//input[@id="su"]/@value')[0]

print(value)