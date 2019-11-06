import random
import time
from other.Commonlib import Commonshare

from user_Script.test_report import Test_report
import unittest
from selenium import webdriver


class Testcace_report(unittest.TestCase):
    """# 预报舱单申报模块"""

    def save_img(self, img_name):
        pass

    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('bye')

    # 更改密码
    def test_1000(self):
        """更改密码"""
        log = Test_report()
        log.login('customer1', '123456')
        log.update_mm()

    # 待发送--查询
    def test_0001(self):
        """待发送--查询"""
        log = Test_report()
        log.login('customer1', '123456')
        log.query('TEST123', 'SH', 'SH', 's')

    def test_0002(self):
        """ 待发送-- 新增 > 创建"""
        add = Test_report()
        add.login('customer1', '123456')
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.add_creat(TDH, num, num)

    # 待发送-- 新增 > 暂存
    def test_0003(self):
        """待发送-- 新增 > 暂存"""
        add = Test_report()
        add.login('customer1', '123456')
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.temporary_add(TDH, num, num)

    # 待发送-- 新增 > 发送
    def test_0004(self):
        """待发送-- 新增 > 发送"""
        add = Test_report()
        add.login('customer1', '123456')
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        add.seed(TDH, num, num)

    # 待发送--导入
    def test_0005(self):
        """待发送--导入"""
        im = Test_report()
        im.login('customer1', '123456')
        im.import_excel()

    # 待发送--批量发送
    def test_0006(self):
        """待发送--批量发送"""
        se = Test_report()
        se.login('customer1', '123456')
        se.seed_more()

    # 待发送-- 修改
    def test_0007(self):
        """待发送-- 修改"""
        update = Test_report()
        update.login('customer1', '123456')
        num = str(random.randint(1, 1000))
        print(num)
        TDH = 'ex' + num
        update.update_wait_seed(TDH, num, num)

    # 代发送-- excel查看
    def test_0008(self):
        """代发送-- excel查看"""
        excel = Test_report()
        excel.login('customer1', '123456')
        excel.excel_history()

    # 待发送--删除
    def test_0009(self):
        """待发送--删除"""
        rm = Test_report()
        rm.login('customer1', '123456')
        rm.rm_wait_seed()

    # 已发送--查询
    def test_0010(self):
        """已发送--查询"""
        se = Test_report()
        se.login('customer1', '123456')
        se.select_seed('Z236027781', 'Z236027782', 'YM PLUM', '157W')

    # 已发送--修改
    def test_0013(self):
        """已发送--修改"""
        update = Test_report()
        update.login('customer1', '123456')
        update.update_seed()

    #  已发送--复制新增 > 暂存
    def test_0014(self):
        """已发送--复制新增 > 暂存"""
        log = Test_report()
        log.login('customer1', '123456')

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

    #  已发送--复制新增 > 发送
    def test_0016(self):
        """已发送--复制新增 > 发送"""
        log = Test_report()
        log.login('customer1', '123456')

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

    # 已发送--excel 查看
    def test_0017(self):
        """已发送--excel 查看"""
        ex = Test_report()
        ex.login('customer1', '123456')
        ex.excel_history_seed()
        # 复制新增

    # 已发送--报文历史查看
    def test_0018(self):
        """已发送--报文历史查看"""
        re = Test_report()
        re.login('customer1', '123456')
        re.report_history()

    # 导入EDI舱单报文
    def test_0019(self):
        """导入EDI舱单报文"""
        log = Test_report()
        log.login('customer1', '123456')
        log.import_edi()

    # EDI 解析记录
    def test_0020(self):
        """EDI 解析记录"""
        log = Test_report()
        log.login('customer1', '123456')
        log.record_edi()

    # 代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回
    def test_0021(self):
        """代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回"""
        log = Test_report()
        log.login('customer1', '123456')
        log.manifest_management()

    # 代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息
    def test_0022(self):
        """代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息"""
        log = Test_report()
        log.login('customer1', '123456')
        log.manifest_management01()

    # 港口代码参照表下载，舱单模板下载
    def test_0023(self):
        """港口代码参照表下载，舱单模板下载"""
        log = Test_report()
        log.login('customer1', '123456')
        log.down_db()


if __name__ == '__main__':
    unittest.main()
