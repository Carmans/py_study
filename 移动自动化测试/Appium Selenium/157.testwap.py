# encoding:utf-8
from appium import webdriver
import time
# 定义初始化的属性信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['browserName'] = 'Browser'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#打开首页
driver.get("http://www.imooc.com")
time.sleep(3)

#验证实战标签显示了
e = driver.find_element_by_xpath('//*[@id="pages-container"]/section[2]/ul/li[1]/a/span')
#断言显示了
assert e.is_displayed()
driver.quit()
