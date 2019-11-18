import time
import unittest
from selenium import webdriver

from other.BeautifulReport import BeautifulReport
from other.Commonlib import Commonshare


class TestcaseMoney(unittest.TestCase):
    """费用管理"""

    def setUp(self) -> None:
        opt = webdriver.ChromeOptions()
        opt.headless = True
        self.driver = webdriver.Chrome(options=opt)
        self.driver.set_window_size(1920, 1080)
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        driver = self.driver
        driver.find_element_by_name('USERNAME').send_keys('customer1')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        driver.maximize_window()
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\image\\%s.png" % img_name)

    def tearDown(self) -> None:
        """关闭浏览器"""
        self.driver.quit()

    @BeautifulReport.add_test_img('费用管理')
    def test_0001(self):
        """费用管理"""
        from user_script.test_money import TestMoney
        log = TestMoney(self.driver)
        log.test_money()
        self.save_img('费用管理')
