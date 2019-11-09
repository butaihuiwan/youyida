import random
import time
import unittest
from selenium import webdriver
from user_script.test_report import TestReport
from admin_script.test_track_admin import TestTrackAdmin
from other.BeautifulReport import BeautifulReport
from admin_script.test_manage import TestManage


class CaseTrackAdmin(unittest.TestCase):
    """预备舱单申报"""

    def setUp(self):
        """登陆管理员账号"""
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        self.driver.maximize_window()
        driver = self.driver
        # 设置隐士等待时间 10s
        driver.implicitly_wait(10)
        driver.find_element_by_name('USERNAME').send_keys('company')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\image\\%s.png" % img_name)

    def tearDown(self) -> None:
        """关闭浏览器"""
        self.driver.quit()
        time.sleep(2)

    @BeautifulReport.add_test_img('待发送-查询')
    def test_0001(self):
        """申报预备舱单：待发送-查询"""
        TestReport(self.driver).query()
        self.save_img('待发送-查询')

    @BeautifulReport.add_test_img('新增创建')
    def test_0002(self):
        """申报预备舱单：待发送-新增-创建"""
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        TestReport(self.driver).add_creat('管理员账号', TDH, num, num)
        self.save_img('新增创建')

    @BeautifulReport.add_test_img('新增暂存')
    def test_0003(self):
        """待发送-- 新增 > 暂存"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.temporary_add('管理员账号', TDH, num, num)
        self.save_img('新增暂存')

    @BeautifulReport.add_test_img('新增发送')
    def test_0004(self):
        """待发送-- 新增 > 发送"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.seed('管理员账号', TDH, num, num)
        self.save_img('新增发送')

    @BeautifulReport.add_test_img('导入')
    def test_0005(self):
        """待发送--导入"""
        im = TestReport(self.driver)
        im.import_excel()
        self.save_img('导入')

    @BeautifulReport.add_test_img('批量发送')
    def test_0006(self):
        """待发送--批量发送"""
        se = TestReport(self.driver)
        se.seed_more()
        self.save_img('批量发送')

    # # @BeautifulReport.add_test_img('待发送--修改')
    # def test_0007(self):
    #     """待发送-- 修改"""
    #     update = TestReport(self.driver)
    #     num = str(random.randint(1, 1000))
    #     print(num)
    #     TDH = 'ex' + num
    #     update.update_wait_seed("管理员账号", TDH, num, num)
    #     # self.save_img('待发送--修改')
