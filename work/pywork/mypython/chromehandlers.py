from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 设置chrome浏览器的安装路径
path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_options.binary_location = path

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("https://www.baidu.com")

# 输出快照
browser.save_screenshot("baidu.jpg")