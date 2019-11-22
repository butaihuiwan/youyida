import random
import time

from selenium import webdriver

from other.BeautifulReport import BeautifulReport
from other.Commonlib import Commonshare

from user_script.test_track import TestTrack
import unittest
from other.BeautifulReport import BeautifulReport


class TestcaseTrack(unittest.TestCase):
    """数据服务"""

    def setUp(self) -> None:
        # opt = webdriver.ChromeOptions()
        # opt.headless = True
        # self.driver = webdriver.Chrome(options=opt)
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        driver = self.driver
        driver.find_element_by_name('USERNAME').send_keys('customer1')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        self.driver.set_window_size(1920, 1080)
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()


    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\image\\%s.png" % img_name)

    def tearDown(self) -> None:
        self.driver.quit()

    @BeautifulReport.add_test_img('口岸数据')
    def test_0001(self):
        """ 口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比"""
        log = TestTrack(self.driver)
        log.query_track()
        self.save_img('口岸数据')

    @BeautifulReport.add_test_img('新舱单节点查询导入模板下载')
    def test_0002(self):
        """新舱单节点查询导入模板下载"""
        log = TestTrack(self.driver)
        log.down_db()
        self.save_img('新舱单节点查询导入模板下载')

    @BeautifulReport.add_test_img('查验数据')
    def test_0003(self):
        """查验数据: 查询 > 添加订阅 > 批量订阅 > 重置"""
        log = TestTrack(self.driver)
        log.check()
        self.save_img('查验数据')

    @BeautifulReport.add_test_img('查验数据查询导入模板下载')
    def test_0004(self):
        """查验数据查询导入模板下载"""
        log = TestTrack(self.driver)
        log.down_cd()
        self.save_img('查验数据查询导入模板下载')
