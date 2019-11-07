import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from other.Commonlib import Commonshare
from .test_report import Test_report
from selenium.webdriver import ActionChains


# 费用管理: 费用账单， 水单管理
class Test_money(Test_report):
    """ 费用账单: 预配舱单计费 > 口岸数据服务计费 > 港区数据服务计费 > 查询数据服务计费"""

    def test_money(self):
        driver = self.driver
        driver.find_element_by_link_text('费用管理').click()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-09-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[1]/div/form/div/div[1]/div[3]/a').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '预配舱单计费查询')
        driver.find_element_by_xpath('//*[@id="downloadBtn"]').click()

        # 口岸数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-09-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[2]/div/form/div/div[1]/div[3]/a').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '口岸数据服务计费查询')

        # 港区数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-08-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[3]/div/form/div/div[1]/div[3]/a').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '港区数据服务计费')

        # 查验数据服务计费
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[1]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[1]').send_keys(
            '2019-08-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[2]').clear()
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[1]/div/input[2]').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath(
            '//*[@id="column-container"]/div[2]/div/div/div/div/div/div[4]/div/form/div/div[1]/div[3]/a').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '查验数据服务计费')

        # 水单管理：查看水单 > 上传
        driver.find_element_by_link_text('水单管理').click()
        driver.find_element_by_xpath('//*[@id="exchangeListTable"]/tbody/tr[1]/td[8]/a').click()
        self.el_show(self, 'xpath', '//*[@id="detailDiv"]/img')
        el = driver.find_element_by_xpath('//*[@id="detailDiv"]/img')
        url = el.get_attribute('scr')
        print(url)
        try:
            driver.get(url)
            print('ok')
        except:
            print('水单图片查看失败')
        finally:
            pass

        driver.find_element_by_link_text('确定').click()

        # 上传
        driver.find_element_by_link_text('上传').click()
        driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[1]/div/div/input').send_keys(
            '100')
        driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input').send_keys(
            '2019-10-30')
        driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[2]/div/div/input').click()
        driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[3]/div/div/input').send_keys(
            '100')
        el = driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[1]/div/div/div/div[4]/div/div/select')
        select = Select(el)
        select.select_by_visible_text('代付')
        el = driver.find_element_by_xpath('//*[@id="uploadImg"]')
        time.sleep(2)
        ActionChains(driver).move_to_element(el).move_by_offset(5, 5).click().perform()
        time.sleep(2)

        """上传图片"""
        os.system(r'D:\模板文件\test.exe "D:\模板文件\水单.jpg"')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="exchangeEditForm"]/div[2]/button').click()
