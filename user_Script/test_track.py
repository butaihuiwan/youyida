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
from .test_report import Test_report


# 物流节点跟踪
class Test_track(Test_report):

    # 口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比
    def query_track(self):
        driver = self.driver
        driver.find_element_by_link_text('物流节点跟踪').click()
        driver.find_element_by_link_text('口岸数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="BILL_NBR"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARGE_NAM"]').send_keys('W')
        driver.find_element_by_xpath('//*[@id="BARG_VOYAGE_NO"]').send_keys('WW')
        driver.find_element_by_link_text('查询').click()
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[4]')
        driver.find_element_by_link_text('重置').click()
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[8]/a').click()
        Test_track.el_show(self, 'text', '取消', '取消')
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)
        Test_track.el_show(self, 'text', '批量订阅', '批量订阅')

        driver.find_element_by_link_text('批量订阅').click()
        time.sleep(1)
        os.system(r'D:\模板文件\test.exe "D:\模板文件\新舱单节点查询导入模板.xlsx"')
        Test_track.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '提示')

        Test_track.compare_el(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '*成功', '批量订阅')

    # 新舱单节点查询导入模板下载
    def down_qb(self):
        driver = self.driver
        driver.find_element_by_link_text('物流节点跟踪').click()
        driver.find_element_by_link_text('新舱单节点查询导入模板下载').click()

    # 查验数据: 查询 > 添加订阅 > 批量订阅 > 重置
    def check(self):
        driver = self.driver
        driver.find_element_by_link_text('物流节点跟踪').click()
        driver.find_element_by_link_text('查验数据').click()
        js = 'document.getElementById("from").value = "2018-09-08"'
        driver.execute_script(js)
        driver.find_element_by_link_text('查询').click()
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[2]')

        driver.find_element_by_link_text('重置').click()

    # 查验数据查询导入模板下载
    def down_cd(self):
        driver = self.driver
        driver.find_element_by_link_text('物流节点跟踪').click()
        driver.find_element_by_link_text('查验数据').click()
        driver.find_element_by_link_text('查验数据查询导入模板下载').click()
