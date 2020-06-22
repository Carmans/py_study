#encoding: utf-8
from selenium import webdriver
import time

#打开chrome浏览器
driver = webdriver.Chrome()
#输入慕课网首页地址
driver.get("http://www.imooc.com")
#等待页面完全加载完
time.sleep(3)
#定位实战tab
tab = driver.find_element_by_xpath('//*[@id="nav"]/ul/li[4]/a')
#点击
tab.click()
#等待页面加载完
time.sleep(3)
#断言文案"后端开发"显示了
content = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/a[3]')
assert u"后端开发" in content.text
#退出
driver.quit()