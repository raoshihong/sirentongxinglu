from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.baidu.com"
# 在mac下如果驱动在bin目录或者path环境下可以不用写路径
brower = webdriver.Chrome()

# 打开浏览器
brower.get(url)

# 睡2s
time.sleep(20)

# 获取输入框
# wdInput = brower.find_element_by_id("kw")

wdInput = brower.find_element(by=By.ID,value="kw")
# 给输入框设置数据
wdInput.send_keys("冬季")

# 睡2s
time.sleep(20)

# 获取百度以下点击按钮
btn = brower.find_element(by=By.ID,value='su')
# 触发点击
btn.click()

time.sleep(20)

# 执行js代码,让浏览器滚动
js = 'document.documentElement.scrollTop = 100000'
brower.execute_script(js)

time.sleep(20)

# 点击下一页
nextPageBtn = brower.find_element(by=By.CLASS_NAME,value='n')
print(nextPageBtn)
nextPageBtn.click()

time.sleep(20)
brower.back()