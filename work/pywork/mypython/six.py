import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")

# print(type(response))

# 读取获取到的结果,返回的是一个二进制
# print(response.read())

# 对结果进行解码
# print(response.read().decode("UTF-8"))

# 读取指定个字符
# print(response.read(5))

# 读取一行
# print(response.readline())

# 读取多行
# print(response.readlines())

# 获取请求的响应编码
# print(response.getcode())

# 获取请求的url
# print(response.geturl())

# 获取头部信息
# print(response.getheaders())




# 下载

# 下载网页
# url = "http://www.baidu.com"
# # 第一个参数为地址,第二参数为文件名
# urllib.request.urlretrieve(url, "baidu.html")

# 下载图片 [https的地址可能需要证书,此时可以使用request模拟浏览器]
# url = "http://img1.baidu.com/it/u=322908874,1639341413&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=583"
# urllib.request.urlretrieve(url,"aa.jpeg")

# 下载视频
# url = "http://vd3.bdstatic.com/mda-kjtx64epufgk8zw5/sc/cae_h264_nowatermark/1604104149/mda-kjtx64epufgk8zw5.mp4?v_from_s=hkapp-haokan-hna&auth_key=1650710528-0-0-943b5c23ecc1d0b9c15531c6cbd1514d&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0727931759&vid=6647036806223333961&abtest=100815_2-101454_3-17451_2&klogid=0727931759"
# urllib.request.urlretrieve(url, "aa.mp4")

