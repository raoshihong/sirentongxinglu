import urllib.request
import ssl

from lxml import etree

 # 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def getContent(currentPage):
    url = "https://sc.chinaz.com/tupian/nvshengtupian.html"
    if currentPage>1:
        url = "https://sc.chinaz.com/tupian/nvshengtupian_"+str(currentPage)+".html"
    request = urllib.request.Request(url=url)
    response = urllib.request.urlopen(request)
    content = response.read().decode("UTF-8")
    return content

def downloadImage(content):
    tree = etree.HTML(content)
    # names = tree.xpath('//div[@id="container"]//a/img//@alt')
    # 一般网络图片都有懒加载,所以需要注意图片的获取
    """
    图片没加载时是放到src2,当滑动到图片位置时则会自动替换到src属性上
    <a href="//sc.chinaz.com/tupian/210128146623.htm" target="_blank" alt="亚洲清纯女生图片">
        	<img src2="//scpic3.chinaz.net/Files/pic/pic9/202101/apic30396_s.jpg" alt="亚洲清纯女生图片" class="">
        	</a>
    """
    # srcs = tree.xpath('//div[@id="container"]//a/img//@src2')

    imgs = tree.xpath('//div[@id="container"]//a/img')

    for img in imgs:
        name = img.xpath('@alt')[0]
        src = img.xpath('@src2')[0]
        if src == '':
            src = img.xpath('@src')[0]
        urllib.request.urlretrieve(url = "https:"+src,filename="images/"+name+".jpg")

if __name__ == '__main__':
    for currentPage in range(1,10):
        downloadImage(getContent(currentPage))