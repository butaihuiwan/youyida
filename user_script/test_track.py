import os
import random
import time
from selenium import webdriver
from other.Commonlib import Commonshare
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .test_report import TestReport


class TestTrack(Commonshare):
    """物流节点跟踪"""

    def query_track(self):
        """口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比"""
        driver = self.driver
        driver.find_element_by_link_text('数据服务').click()
        driver.find_element_by_link_text('口岸数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="BILL_NBR"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARGE_NAM"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARG_VOYAGE_NO"]').send_keys('WW')
        driver.find_element_by_link_text('查询').click()
        TestReport.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[4]')
        driver.find_element_by_link_text('重置').click()
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[8]/a').click()
        TestTrack.el_show(self, 'text', '取消', '取消')
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)
        TestTrack.el_show(self, 'text', '批量订阅', '批量订阅')
        time.sleep(2)
        # js = 'document.getElementByClassName(" icon-action-new ").click();'
        # driver.execute_script(js)

        driver.find_element_by_link_text('批量订阅').send_keys(Keys.ENTER)
        time.sleep(1)
        os.system(r'D:\模板文件\test.exe "D:\模板文件\新舱单节点查询导入模板.xlsx"')
        self.el_show('css', '#toast-container > div > div.toast-message', '提示')
        TestTrack.compare_el(self, 'css', '#toast-container > div > div.toast-message', '*成功', '批量订阅')

    def down_db(self):
        """新舱单节点查询导入模板下载"""
        driver = self.driver
        driver.find_element_by_link_text('数据服务').click()
        driver.find_element_by_link_text('新舱单节点查询导入模板下载').click()

    def check(self):
        """ 查验数据: 查询 > 添加订阅 > 批量订阅 > 重置"""
        driver = self.driver
        driver.find_element_by_link_text('数据服务').click()
        driver.find_element_by_link_text('查验数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_link_text('查询').click()
        TestReport.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[2]')

        driver.find_element_by_link_text('重置').click()

    def down_cd(self):
        """查验数据查询导入模板下载"""
        driver = self.driver
        driver.find_element_by_link_text('数据服务').click()
        driver.find_element_by_link_text('查验数据').click()
        driver.find_element_by_link_text('查验数据查询导入模板下载').click()
