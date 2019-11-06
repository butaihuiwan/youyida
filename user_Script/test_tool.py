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


# # 综合工具：船代快速通道 > 船舶位置查询 > HS商品编码查询 > 快递查询 > 远期运价 > 海运货物跟踪
# class Test_tool(Test_report):
#     # 船代快速通道 > 船舶位置查询 > HS商品编码查询 > 快递查询 > 远期运价 > 海运货物跟踪
#     def test_tools(self):
#         driver = self.driver
#         driver.find_element_by_link_text('综合工具').click()
#         driver.find_element_by_xpath('//*[@id="BoatFast"]').click()
#         driver.find_element_by_xpath('//*[@id="BoatPosition"]').click()
#         el = (By.XPATH, '//*[@id="GoodsNo"]')
#         try:
#             WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(el))
#             print('加载出来了')
#         except:
#             print('加载失败')
#         # driver.find_element_by_xpath('//*[@id="GoodsNo"]').click()
#         # time.sleep(2)
#         driver.find_element_by_xpath('//*[@id="Fast"]').click()
#         driver.find_element_by_xpath('//*[@id="Trace"]').click()
