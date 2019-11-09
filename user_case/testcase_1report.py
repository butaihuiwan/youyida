import random
import time
from other.Commonlib import Commonshare
from other.BeautifulReport import BeautifulReport
from user_script.test_report import TestReport
import unittest
from selenium import webdriver


class TestcaseReport(unittest.TestCase):
    """预报舱单申报模块"""

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        driver = self.driver
        driver.find_element_by_name('USERNAME').send_keys('customer1')
        driver.find_element_by_name('PASSWORD').send_keys('123456')
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file("C:\\Users\\wh\\PycharmProjects\\youyida\\suit\\image\\%s.png" % img_name)

    def tearDown(self) -> None:
        print('bye')

    # 更改密码
    @BeautifulReport.add_test_img('更改密码')
    def test_1000(self):
        """更改密码"""

        log = TestReport(self.driver)
        log.update_mm()
        self.save_img('更改密码')

    # 待发送--查询
    @BeautifulReport.add_test_img('待发送-查询')
    def test_0001(self):
        """待发送--查询"""
        log = TestReport(self.driver)
        log.query('TEST123', 'SH', 'SH', 's')
        self.save_img('待发送-查询')

    @BeautifulReport.add_test_img('待发送-- 新增 > 创建')
    def test_0002(self):
        """ 待发送-- 新增 > 创建"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.add_creat('测试账号1', TDH, num, num)
        self.save_img('待发送-- 新增 > 创建')

    # 待发送-- 新增 > 暂存
    @BeautifulReport.add_test_img('待发送-- 新增 > 暂存')
    def test_0003(self):
        """待发送-- 新增 > 暂存"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.temporary_add('测试账号1', TDH, num, num)
        self.save_img('待发送-- 新增 > 暂存')

    # 待发送-- 新增 > 发送
    @BeautifulReport.add_test_img('待发送-- 新增 > 发送')
    def test_0004(self):
        """待发送-- 新增 > 发送"""
        add = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.seed(TDH, num, num)
        self.save_img('待发送-- 新增 > 发送')

    # 待发送--导入
    @BeautifulReport.add_test_img('待发送--导入')
    def test_0005(self):
        """待发送--导入"""
        im = TestReport(self.driver)
        im.import_excel()
        self.save_img('待发送--导入')

    # 待发送--批量发送
    @BeautifulReport.add_test_img('待发送--批量发送')
    def test_0006(self):
        """待发送--批量发送"""
        se = TestReport(self.driver)
        se.seed_more()
        self.save_img('待发送--批量发送')

    # 待发送-- 修改
    @BeautifulReport.add_test_img('待发送--修改')
    def test_0007(self):
        """待发送-- 修改"""
        update = TestReport(self.driver)
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        update.update_wait_seed("测试账号1", TDH, num, num)
        self.save_img('待发送--修改')

    # 代发送-- excel查看
    @BeautifulReport.add_test_img('待发送--excel查看')
    def test_0008(self):
        """代发送-- excel查看"""
        excel = TestReport(self.driver)
        excel.excel_history()
        self.save_img('待发送--excel查看')

    # 待发送--删除
    @BeautifulReport.add_test_img('待发送--删除')
    def test_0009(self):
        """待发送--删除"""
        rm = TestReport(self.driver)
        rm.rm_wait_seed()
        self.save_img('待发送--删除')

    # 已发送--查询
    @BeautifulReport.add_test_img('已发送--查询')
    def test_0010(self):
        """已发送--查询"""
        se = TestReport(self.driver)
        se.select_seed('Z236027781', 'Z236027782', 'YM PLUM', '157W')
        self.save_img('已发送--查询')

    # 已发送--修改
    @BeautifulReport.add_test_img('已发送--修改')
    def test_0013(self):
        """已发送--修改"""
        update = TestReport(self.driver)
        update.update_seed()
        self.save_img('已发送--修改')

    #  已发送--复制新增 > 暂存
    @BeautifulReport.add_test_img('已发送--复制新增 > 暂存')
    def test_0014(self):
        """已发送--复制新增 > 暂存"""
        log = TestReport(self.driver)

        # 断言，判断登陆页面用户账号的属性值是否相同
        try:
            # 获取登陆用户名显示元素属性
            data = log.get_attr('xpath',
                                '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div/div/div[2]/p[2]/label',
                                'class')
            print(data)
            self.assertEqual('label label-info', data)
        except Exception as e:
            print('测试失败', format(e))
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'TEST' + num
        log.copy_add01(TDH, num, num)
        self.save_img('已发送--复制新增 > 暂存')

    @BeautifulReport.add_test_img('已发送--复制新增 > 发送')
    def test_0016(self):
        """已发送--复制新增 > 发送"""
        log = TestReport(self.driver)

        # 断言，判断登陆页面用户账号的属性值是否相同
        try:
            # 获取登陆用户名显示元素属性
            data = log.get_attr('xpath',
                                '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div/div/div[2]/p[2]/label',
                                'class')
            print(data)
            self.assertEqual('label label-info', data)
        except Exception as e:
            print('测试失败', format(e))
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'TEST' + num
        log.copy_add03(TDH, num, num)
        self.save_img('已发送--复制新增 > 发送')

    @BeautifulReport.add_test_img('已发送--excel 查看')
    def test_0017(self):
        """已发送--excel 查看"""
        ex = TestReport(self.driver)
        ex.excel_history_seed()
        self.save_img('已发送--excel 查看')

    @BeautifulReport.add_test_img('已发送--报文历史查看')
    def test_0018(self):
        """已发送--报文历史查看"""
        re = TestReport(self.driver)
        re.report_history()
        self.save_img('已发送--报文历史查看')

    @BeautifulReport.add_test_img('导入EDI舱单报文')
    def test_0019(self):
        """导入EDI舱单报文"""
        log = TestReport(self.driver)
        log.import_edi()
        self.save_img('导入EDI舱单报文')

    @BeautifulReport.add_test_img('EDI解析记录')
    def test_0020(self):
        """EDI解析记录"""
        log = TestReport(self.driver)
        log.record_edi()
        self.save_img('EDI解析记录')

    @BeautifulReport.add_test_img('代发舱单管理--待处理')
    def test_0021(self):
        """代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回"""
        log = TestReport(self.driver)
        log.manifest_management()
        self.save_img('代发舱单管理--待处理')

    @BeautifulReport.add_test_img('代发舱单管理--已处理')
    def test_0022(self):
        """代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息"""
        log = TestReport(self.driver)
        log.manifest_management01()
        self.save_img('代发舱单管理--已处理')

    @BeautifulReport.add_test_img('舱单模板下载')
    def test_0023(self):
        """港口代码参照表下载，舱单模板下载"""
        log = TestReport(self.driver)
        log.down_db()
        self.save_img('舱单模板下载')


if __name__ == '__main__':
    unittest.main()
