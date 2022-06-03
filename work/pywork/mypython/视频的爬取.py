# 现在的视频,一般都会做分片处理,且每个视频都有高清，1080等清晰度等视频,不再是直接一个视频地址,大部分都会做成m3u8文件保留分片信息
import urllib.request
import ssl

#
# # 请求百度翻译
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://ali2.a.kwimgs.com/udata/music/music_f32d50555d764e559c29b5188e0fc9530.jpg"

headers = {
    # ':authority': 'vip.shankuwang.com:8443',
    # ':method': 'GET',
    # ':path': '/playurl/tu/m3u8?v=396e316542587843527237416d3646794f7a4838714858344c6d4165724670454176395a457a6274657534714e424e6c71304150646b586f68456539672b50354f34654a715551505370416478373371666e323738694d5a4a74654d644b63624854787538342f6b77326a7766585454697477686d6a326f6b52637072572f44&k=027626ee0d48f67c3579b8cf97e69770&s=624838784e3573754b7a7933476e6f55697662684c673d3d&ts=1',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ZH-cn,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" NOt a;brand";v="99", "chromium";v="102", "googLe chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"MAcOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'mozilla/5.0 (macintosH; intEl MAC OS X 10_15_7) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/102.0.5005.61 safari/537.36',
}
request = urllib.request.Request(url = url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read()
print(content)





