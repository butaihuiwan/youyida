import unittest
# from script.test_money import Test_money


class Testcase_money(unittest.TestCase):
    """费用管理"""

    def test_0001(self):
        from script.test_money import Test_money
        """费用管理"""
        log = Test_money()
        log.login('customer1', '123456')
        log.test_money()
