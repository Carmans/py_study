#encoding: utf-8
import unittest
from appium import webdriver
from ddt import ddt,data
import time

@ddt
class MyTestCase(unittest.TestCase):
    #初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.102:5555'
        desired_caps['browserName'] = 'Browser'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #释放资源
    def tearDown(self):
        self.driver.quit()

    @data(u"Android 专项测试 Python篇", u"Javacript")
    def test_searchkeyword(self, keyword):
        #打开首页
        self.driver.get("http://www.imooc.com")
        #等待加载完成
        time.sleep(3)
        #定位输入框
        input = self.driver.find_element_by_xpath("/html/body/header/div/form/div/input")
        #输入关键词
        input.send_keys(keyword)
        #定位搜索按钮
        button = self.driver.find_element_by_xpath("/html/body/header/div/form/div/div/button")
        #点击搜索
        button.click()
        #等待页面加载完成
        time.sleep(3)
        #定位搜索结果的首条
        result0 = self.driver.find_element_by_xpath('//*[@id="pages-container"]/div/div[1]/dl/dd[1]/a/div/p[1]')
        #验证包含关键词
        self.assertTrue(keyword in result0.text)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTests(cases)
    myTestRunner = unittest.TextTestRunner(verbosity=2)
    myTestRunner.run(suite)
