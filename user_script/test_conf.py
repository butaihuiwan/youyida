import random
import time
from selenium.webdriver.common.keys import Keys
from other.Commonlib import Commonshare
from user_script.test_report import TestReport


# 基础配置
class Test_conf(Commonshare):
    """
    查询 > 新增 > 邮箱管理 > 手机号管理 >
    账号操作：口岸服务 > 港区服务 > 查验服务
    """
    def test_conf(self):
        driver = self.driver
        driver.find_element_by_link_text('基础配置').click()
        driver.find_element_by_xpath('//*[@id="form"]/div/div[1]/div[4]/div/input').send_keys('00000009')
        driver.find_element_by_link_text('查询').click()
        TestReport.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[1]')
        time.sleep(5)

        driver.find_element_by_link_text('新增').click()
        driver.find_element_by_xpath('//*[@id="companyName"]').send_keys('测试账号一子账号六')
        num = str(random.randint(1, 100))
        driver.find_element_by_xpath('//*[@id="secLoginName"]').send_keys('customer' + num)
        driver.find_element_by_xpath('//*[@id="secPassword"]').send_keys('123456')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="text-body"]/div/div/a[2]').click()
        """断言是否出现提示该账号已存在提示"""
        self.compare_el('xpath', '//*[@id="toast-container"]/div[2]/div[2]', '存在', '账号新增')

        self.el_show('text', '邮箱管理', '邮箱管理点击加载')
        driver.find_element_by_link_text('邮箱管理').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('12345678@qq.com')
        time.sleep(5)
        driver.find_element_by_css_selector('.doAddEmail').click()
        """断言是否出现提示邮箱变更成功提示"""
        self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '邮箱新增')

        time.sleep(5)
        self.el_show('css', '#emailList > p:nth-child(1) > a', '删除点击加载')
        driver.find_element_by_css_selector('#emailList > p:nth-child(1) > a').click()
        self.el_show('css', '.modal-footer > .btn-primary', '确认点击加载')
        driver.find_element_by_css_selector('.modal-footer > .btn-primary').click()
        """断言是否出现提示邮箱删除成功提示"""
        self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '邮箱删除')
        self.el_show('css', '#addEmailDialog > .close', '关闭点击加载')
        time.sleep(2)
        driver.find_element_by_css_selector('#addEmailDialog > .close').click()

        time.sleep(5)
        self.el_show('text', '手机号管理', '手机号管理点击加载')
        driver.find_element_by_link_text('手机号管理').click()
        driver.find_element_by_xpath('//*[@id="phoneNumber"]').send_keys(12345678910)
        self.el_show('text', '新增/修改', '新增/修改点击加载')
        driver.find_element_by_link_text('新增/修改').click()
        """断言是否出现提示邮箱删除成功提示"""
        self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '手机号变更')

        time.sleep(5)
        self.el_show('text', '删除', '删除点击点击加载')
        driver.find_element_by_link_text('删除').click()
        self.el_show('xpath', '/html/body/div[8]/div/div/div[2]/button[2]', '删除确认点击加载')
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button[2]').click()
        """断言是否出现提示邮箱删除成功提示"""
        self.compare_el('xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '手机号删除')
        self.el_show('css', '#addPhoneNumberDialog > div.close', '关闭点击点击加载')
        time.sleep(2)
        driver.find_element_by_css_selector('#addPhoneNumberDialog > div.close').click()

        # 账号操作
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[1]', '口岸服务点击加载')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[1]').click()
        TestReport.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '口岸服务点击加载')
        time.sleep(2)

        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[2]', '港区服务点击加载')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[2]').click()
        TestReport.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '港区服务点击加载')
        time.sleep(2)

        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[3]', '查验服务点击加载')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[3]').click()
        TestReport.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '查验服务点击加载')
