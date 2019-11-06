import unittest

from selenium import webdriver

from other.BeautifulReport import BeautifulReport
from other.test01 import Test_report

class Testcace_report(unittest.TestCase):
    """预报舱单申报模块"""

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file(r'C:\Users\wh\PycharmProjects\untitled\suit\image\%s' % img_name)

    def setUp(self) -> None:
        print('start')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        print('bye')

    # 待发送--查询
    @BeautifulReport.add_test_img('test_0001')
    def test_0001(self):
        """登陆"""
        log = Test_report()
        log.login('customer1', '123456')
        self.save_img('test_0001')
