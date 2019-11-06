import time
from other.test_02 import Testcace_report

class Test_report(Testcace_report):
    """预报舱单申报模块"""

    def login(self, user, pwd):
        """普通账号登陆"""
        # 设置浏览器的最大化


        driver.find_element_by_name('USERNAME').send_keys(user)
        driver.find_element_by_name('PASSWORD').send_keys(pwd)
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()
        # 判断
        # Test_report.el_show(self, 'text', '工作台','登陆')
        time.sleep(1)