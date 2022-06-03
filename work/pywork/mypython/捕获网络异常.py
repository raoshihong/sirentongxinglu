import urllib.request

url = "https://www.dushu.com/"
request = urllib.request.Request(url=url)
try:
    urllib.request.urlopen(request)
except Exception as e:
    print("异常",e)