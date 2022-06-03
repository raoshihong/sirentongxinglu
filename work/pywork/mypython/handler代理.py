import random
import urllib.request

import ssl

 # 跳过证书验证
# ssl._create_default_https_context = ssl._create_unverified_context

url = "http://www.baidu.com/s?wd=ip"

headers= {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ZH-cn,zh;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'cookie': 'PSTM=1650631397; BAIDUID=95F2551B1062E427EAFA78AE7EB2BBB8:FG=1; BD_UPN=123253; BIDUPSID=65C93A8B3F6446DEF1D9155966C6AB58; BDUSS=VBUZh5KCZVMNFJcRhLKEfBBB35LFNFmNHHOWG1HyK5wVGHYmg1VflfICzRPb3RPSVFBQUFBJCQAAAAAAAAAAAEAAAc27aEwzoYYxTE5OTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaDiTY2I4rWNiV; BDUSS_BFESS=VBUZh5KCZVMNFJcRhLKEfBBB35LFNFmNHHOWG1HyK5wVGHYmg1VflfICzRPb3RPSVFBQUFBJCQAAAAAAAAAAAEAAAc27aEwzoYYxTE5OTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaDiTY2I4rWNiV; BDSFRCVID_BFESS=M4uojeXrog0lAwvDt3iZUiPPj9EtRXOTdYlTOwxPSP3LGjLvgZJfEg0pT8wIvcA-ebm1OGkKLMoTHp-f_2uxojJg8UtVJEC6Eg0Ptf8g0M5; H_BDCLCKID_SF_BFEss=TbKD_c-mFiVdQTrp-tRF5dCShuFSAJKJB2Q-XPOO3KJSDITPQmOPYRIXWG5i26jIWbRm2mbGylRp8P3y0BB2DuA1y4vpKbjP0eTXoUJ2XMkVdq5MQFCWmr-EbPRiJ-b9Qg-Jbpq7Tt5w8nCFbT7L5hkpbt-q0X-jlTnhVN0MBcK0hi0ljj82e5p0hxRy2dR2aI52B5R_5TrJdNcrDF7TXUi82h5Y05oQaB5aKpbi-lCkocohhj5vyT8SXNoRXX74QC6L3li-0XKkScbKbN5LLXl1Db3JYhlLAmtJslfy2t3oePVOdPJc3Mv30-JDJJQOBKQb0kNGbuqkEQ8cQft20b0eeMtJW6leTBUJVc-Xfik3qbt9btK_bJk8kxoe-N3-KK-XWj52FhvI_p7_bF--dRqY-xor2f3J2NTQlRtxLNCvMuj2e-TXy5K_HUvDJn533gbRoj6mAq7GBQQHqT3M-lQbbN3i-4JmFRrPwB3CWhRv8UBsKKCPBTD02-nBAT-oq6NpaJ5njq5NhmJmB67JD-50EgkJtJ_JjJcs3T88KjjEe-Kk-pNVEP-eX-NzKrvha2kjWNj5KhbMhptu5trM0-t-QQONxPRn3N5rKl75yuJ5qKOsqU6d34-lMxj405otbnbFA4QJ066QerCLhpJVYUaDXnO7bIrlxBrtXp7_2J0wStbkY4oTjXl1DB3jKjvMtGDtVD_2JDD2mCDr-R-_-4_tBh_X5-RLF2dJLl7f54nKdp0Xh-qb5X03DPre-4CTLIL8K4b4yn7XsMTs5MnbwH8ykaBR0MTrqDVZBJQN3kJmfkN6yJJjLDu8LxFd2-bIW2Jl2MBd-T6p_IOg2Mn8m4bB3QoPbTqMjeTXoUJ25dnJHhCgE4Bk-tRYjhL8qUK; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; DelPer=0; BD_CK_SAM=1; PSINO=7; BAIDUID_BFESS=1273C259F57BB2E2545C7802F9416A28:FG=1; BA_HECToR=a40l84ah2l0h81218g1h8f4gu14; ZfY=r8YW62Iq32LhyiQNosxkjDQ:aL6dL5jqoqcce18v2N68:C; BD_HOME=1; BDRCVFR[s4-dAUiwMmN]=i67x6tjHwwYf0; av1_switch_v3=0; ab_sr=1.0.1_yTUXNGM0MTa3MJQ2NDY0N2y2yJRioDgYY2e3ZJg4yZVLnWVMnTjLYJE2mTnMZMU3ZDK4zGQYY2U3oDLMyTqXZJy0nJjHYMi3ZMq1mZzMzMZizDLLNWY4MDq2mMjInZbMZJi4mMMXm2QZZTa4zMVlzDcxmJCWZWi0NJK5ZWu3YMe1MMQ5zTBHOGi2yJIxyTdLyMrHMJQ5ZGY4OGU5ODg1Mg==; aRiadefaUlttheme=undefineD; Rt="z=1&dm=baidu.com&si=nqt3eir8q&ss=l3fimu7g&sl=7&tt=aiv&bcn=httpS%3A%2F%2ffclog.baidu.coM%2floG%2fweirwooD%3ftypE%3dperf&ld=mtc&ul=2cnt&hd=2cp1"; BDRCVfr[feWj1vr5u3D]=i67x6tjHwwYf0; COOKIE_SESSION=64266_0_9_9_17_9_1_1_9_5_0_1_64263_0_2_0_1653116203_0_1653116201%7C9%23834200_504_1651538798%7C9; H_PS_PSSID=36426_36455_36367_34812_35915_36165_35979_36055_36419_36235_26350_36469_36447; H_PS_645eC=b25C9lOM00llzuy0IehF2lgCgeTbV91uaYtJLCAIxaOGz0DJulDppp7Ppzu; baIkeviSitid=fac87705-3648-4741-8807-5002fa5494dd',
    'host': 'www.baidu.com',
    'sec-ch-ua': '" NOt a;brand";v="99", "chromium";v="101", "googLe chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"MAcOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'mozilla/5.0 (macintosH; intEl MAC OS X 10_15_7) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/101.0.4951.64 safari/537.36',
}

request = urllib.request.Request(url=url,headers=headers)

# https://www.kuaidaili.com/ 可以注册快代理,购买代理ip


# proxies = {
#     'http':'39.106.71.115:7890'
# }

# 代理池
proxyArr = [
    {'http':'39.106.71.115:7890'},
    {'http':'39.106.71.115:7890'}
]

proxies = random.choice(proxyArr)

# 创建一个代理handler
handler = urllib.request.ProxyHandler(proxies=proxies)

# 构建opener
opener = urllib.request.build_opener(handler)

# 请求
response = opener.open(request)

content = response.read().decode("UTF-8")

print(content)

with open(file="ip.html",mode="w") as fp:
    fp.write(content)

