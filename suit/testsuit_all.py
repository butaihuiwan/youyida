import unittest
import datetime
from user_case.testcase_1report import TestcaseReport
from user_case.testcase_5money import TestcaseMoney
# 导入形成测试报告模板类
from other.BeautifulReport import BeautifulReport
from user_case.testcase_2track import TestcaseTrack
from other.HTMLTestRunner_cn import HTMLTestRunner
from admin_case.testcase_1manage import CaseManage


class SuitTest(unittest.TestCase):
    def test_suit(self):
        # 设置测试报告的路径，文件名称
        filepath = '../report'
        nowTime = datetime.datetime.now().strftime('%m%d%H%M')
        filename = str(nowTime) + '.html'
        url = filepath + '/' + filename
        print(filename)

        # 测试case目录下所有的测试用例
        test_dir = '../user_case'
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='testcase_*.py')

        # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        result = BeautifulReport(discover)
        result.report(description='悠易达测试报告', filename=filename, log_path=filepath)
