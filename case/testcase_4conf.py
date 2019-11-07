import unittest

from script.test_conf import Test_conf


class Testcase_conf(unittest.TestCase):
    """基础配置"""
    def test_0001(self):
        """基础配置"""
        log = Test_conf()
        log.login('customer1', '123456')
        log.test_conf()