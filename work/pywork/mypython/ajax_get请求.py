import ssl
import urllib.request
import ssl

 # 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def getContent(currentPage):
    url = ""
    if currentPage == 1:
        url = "https://www.dushu.com/book/1188.html"
    else:
        url = "https://www.dushu.com/book/1188_"+str(currentPage)+".html"
    # "https://www.dushu.com/book/1188_3.html"
    request = urllib.request.Request(url=url)
    response = urllib.request.urlopen(request)
    content = response.read().decode("UTF-8")
    with open(file="book/"+str(currentPage)+".html",mode="w") as fp:
        fp.write(content)

if __name__ == '__main__':
    for currentPage in range(1,100):
        getContent(currentPage)

