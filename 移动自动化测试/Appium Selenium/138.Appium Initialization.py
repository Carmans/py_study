# encoding:utf-8
from appium import webdriver

# 定义初始化的属性信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['automationName'] = 'Appium'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()
