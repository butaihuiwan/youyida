import unittest
import datetime
from user_case.testcase_1report import TestcaseReport
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
        # 创建测试套件
        mysuit = unittest.TestSuite()

        # 添加某个类中所有用例
        # mysuit.addTest(unittest.makeSuite(Testcace_report))

        # 执行某个类中指定某些用例
        # 将测试用例放到测试套件中
        case_list = ['test_0001']
        for case in case_list:
            mysuit.addTest(CaseManage(case))

        result = BeautifulReport(mysuit)
        result.report(description='悠易达测试报告', filename=filename, log_path=filepath)

