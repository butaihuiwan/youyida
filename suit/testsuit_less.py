import unittest
import datetime
from case.testcase_1report import Testcace_report
# 导入形成测试报告模板类
from other.BeautifulReport import BeautifulReport
from case.testcase_2track import Testcase_track
from other.HTMLTestRunner_cn import HTMLTestRunner


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
            mysuit.addTest(Testcace_report(case))


        # # 测试case目录下所有的测试用例
        # test_dir = '../case'
        # discover = unittest.defaultTestLoader.discover(test_dir, pattern='testcase_*.py')
        #
        # # 创建测试运行器,设置为每一个测试用例生成测试报告，运行测试套件中的测试用例
        result = BeautifulReport(mysuit)
        result = BeautifulReport(mysuit)
        result.report(description='悠易达测试报告', filename=filename, log_path=filepath)

        # HTMLTestRunner
        # with open(url, 'wb')as f:
        #     HTMLTestRunner(
        #         stream=f,  # 相当于f.write(报告)
        #         title='第一个测试报告',
        #         description='第一个测试报告',
        #         verbosity=2  # 为每个测试用例生成测试报告
        #     ).run(mysuit)
