import random
import time

from other.BeautifulReport import BeautifulReport
from other.Commonlib import Commonshare

from user_Script.test_track import Test_track
import unittest


class Testcase_track(unittest.TestCase):
    """物流节点跟踪"""

    # 口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比
    # @BeautifulReport.add_test_img('test_errors_save_imgs')
    def test_0001(self):
        """ 口岸数据 : 查询 > 添加订阅 > 批量订阅 > 重置 > 舱单运抵对比"""
        log = Test_track()
        log.login('customer1', '123456')
        log.query_track()

    # 新舱单节点查询导入模板下载
    @BeautifulReport.add_test_img('test_errors_save_imgs1')
    def test_0002(self):
        """新舱单节点查询导入模板下载"""
        log = Test_track()
        log.login('customer1', '123456')
        log.down_db()

    # 查验数据: 查询 > 添加订阅 > 批量订阅 > 重置
    def test_0003(self):
        """查验数据: 查询 > 添加订阅 > 批量订阅 > 重置"""
        log = Test_track()
        log.login('customer1', '123456')
        log.check()

    #查验数据查询导入模板下载
    def test_0004(self):
        """查验数据查询导入模板下载"""
        log = Test_track()
        log.login('customer1', '123456')
        log.down_cd()
