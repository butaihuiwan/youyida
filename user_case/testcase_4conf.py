import time
import unittest

from selenium import webdriver

from user_script.test_conf import Test_conf
from other.BeautifulReport import BeautifulReport


class TestcaseConf(unittest.TestCase):
    """基础配置"""

    def setUp(self) -> None:
        opt = webdriver.ChromeOptions()
        opt.headless = True
        self.driver = webdriver.Chrome(options=opt)
        self.driver.set_window_size(1920, 1080)
        # self.driver = webdriver.Chrome()
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
        self.driver.quit()

    @BeautifulReport.add_test_img('基础配置')
    def test_0001(self):
        """基础配置"""
        log = Test_conf(self.driver)
        log.test_conf()
        self.save_img('基础配置')

    @BeautifulReport.add_test_img('基础配置-邮箱管理')
    def test_0002(self):
        Test_conf(self.driver).test_email()
        self.save_img('基础配置-邮箱管理')

    @BeautifulReport.add_test_img('基础配置-手机号管理')
    def test_0003(self):
        Test_conf(self.driver).test_mobile()
        self.save_img('基础配置-手机号管理')