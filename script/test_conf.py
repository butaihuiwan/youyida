from script.test_report import Test_report


# 基础配置
class Test_conf(Test_report):
    """
    查询 > 新增 > 邮箱管理 > 手机号管理 >
    账号操作：口岸服务 > 港区服务 > 查验服务
    """

    def test_conf(self):
        driver = self.driver
        driver.find_element_by_link_text('基础配置').click()
        driver.find_element_by_xpath('//*[@id="form"]/div/div[1]/div[4]/div/input').send_keys('00000009')
        driver.find_element_by_link_text('查询').click()
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[1]')
        driver.find_element_by_link_text('新增').click()
        driver.find_element_by_xpath('//*[@id="companyName"]').send_keys('测试账号一子账号六')
        driver.find_element_by_xpath('//*[@id="secLoginName"]').send_keys('customer1006')
        driver.find_element_by_xpath('//*[@id="secPassword"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="text-body"]/div/div/a[2]').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div[2]/div[2]', '账号新增')

        driver.find_element_by_link_text('邮箱管理').click()
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('12345678@qq.com')
        driver.find_element_by_css_selector('.doAddEmail').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '邮箱新增')
        driver.find_element_by_css_selector('.bg-success:nth-child(4) > a').click()
        driver.find_element_by_css_selector('.modal-footer > .btn-primary').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '邮箱删除')
        driver.find_element_by_css_selector('#addEmailDialog > .close').click()

        driver.find_element_by_link_text('手机号管理').click()
        driver.find_element_by_xpath('//*[@id="phoneNumber"]').send_keys(12345678910)
        driver.find_element_by_link_text('新增/修改').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '手机号变更')
        driver.find_element_by_link_text('删除').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '手机号删除')
        driver.find_element_by_css_selector('.modal-footer > .btn-primary').click()

        # 账号操作
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[1]').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '口岸服务')

        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[2]').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '港区服务')

        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[6]/a[3]').click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '查验服务')
