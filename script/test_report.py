import os
import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from other.Commonlib import Commonshare
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from other.other_script import Data


# 预报舱单申报模块
class Test_report(Data):
    """预报舱单申报模块"""

    def login(self, user, pwd):
        """普通账号登陆"""
        # 设置浏览器的最大化
        self.driver.get('http://192.168.17.50:2090/home/control/main')
        self.driver.maximize_window()
        driver = self.driver
        driver.find_element_by_name('USERNAME').send_keys(user)
        driver.find_element_by_name('PASSWORD').send_keys(pwd)
        time.sleep(1)
        login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
        login.click()
        # 判断
        Test_report.el_show(self, 'text', '工作台', '登陆')
        time.sleep(1)

    # 修改密码
    def update_mm(self):
        """修改密码"""
        driver = self.driver
        el = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[3]/a')
        # driver.move_to_element('')
        ActionChains(driver).move_to_element(el).perform()
        driver.find_element_by_link_text('更改密码').click()
        driver.find_element_by_xpath('//*[@id="currentPassword"]').send_keys('123456')
        driver.find_element_by_id('newPassword').send_keys('123456')
        driver.find_element_by_id('newPasswordVerify').send_keys('123456')
        driver.find_element_by_link_text('确定').click()
        time.sleep(1)
        # 判断是否加载出提示成功信息
        Test_report.compare_el(self, 'xpath', '/html/body/div[6]/div/div/div[1]/div', '成功', '修改密码')

    def logout(self):
        """注销"""
        driver = self.driver
        el = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[3]/a')
        ActionChains(driver).move_to_element(el).perform()
        driver.find_element_by_link_text('注销').click()
        # 判断
        Test_report.el_show(self, 'text', '登陆', '注销')

    def query(self, TDH, YDH, CM, HC):
        """
        申报预备舱单查询--待发送
           TDH = 提单号；YDH = 运编号；
           CM = 船名；   HC = 航次
           """
        self.driver.find_element_by_link_text('预配舱单申报').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()

        self.driver.find_element_by_id('from').click()
        self.driver.find_element_by_css_selector('tr:nth-child(2) > .day:nth-child(2)').click()
        self.driver.find_element_by_name('billnbr').send_keys(TDH)
        self.driver.find_element_by_name('freightnbr').send_keys(YDH)
        self.driver.find_element_by_name('shipnam').send_keys(CM)
        self.driver.find_element_by_name('voyageno').send_keys(HC)
        self.driver.find_element_by_link_text('查询').click()
        Test_report.el_show(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[10]/a[1]', '待发送-查询')
        time.sleep(2)

    def add_box(self, TDH, CM, HC):
        """修改时数据"""

        self.data_clear(TDH, CM, HC)
        self.add_data(TDH, CM, HC)

    def add_creat(self, TDH, CM, HC):
        """
        新增--待发送 > 创建
               :param TDH: 提单号
            :param CM: 船名
               :param HC: 航次
               :return:
               """
        self.driver.find_element_by_link_text('预配舱单申报').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(1)
        # 选择发送人代码
        element = self.driver.find_element_by_id('BILL_SENDER_CODE')
        select = Select(element)
        select.select_by_visible_text('测试账号1')
        time.sleep(1)
        # 选择接受人代码
        element = self.driver.find_element_by_id('BILL_RECEIVER_CODE')
        select = Select(element)
        select.select_by_visible_text('民生船代')
        # 订舱信息
        self.driver.find_element_by_id('BILL_NBR').send_keys(TDH)
        self.driver.find_element_by_id('E_SHIP_NAM').send_keys(CM)
        self.driver.find_element_by_id('OUT_VOYAGE_NO').send_keys(HC)
        # 承运人代码
        self.driver.find_element_by_id('TRUST_INFO').send_keys('YML：阳明')
        # 发货人代码
        self.driver.find_element_by_id('SHIPPER_COD').send_keys('USCI+91320412MA1MGBN10R')
        # 收货人代码
        self.driver.find_element_by_id('CONSIGNEE_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
        # 通知人代码
        self.driver.find_element_by_id('NOTIFY_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
        self.driver.find_element_by_link_text('创建').click()
        # 判断创建成功点击确定按钮是否加载出来
        Test_report.el_show(self, 'xpath', '/html/body/div[8]/div/div/div[1]/div', '待发送新增-创建')

    # 新增--待发送 > 暂存
    def temporary_add(self, TDH, CM, HC):
        """
        新增--待发送 > 暂存
        :param TDH: 提单号
     :param CM: 船名
        :param HC: 航次
        :return:
        """
        self.driver.find_element_by_link_text('预配舱单申报').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(1)
        Test_report.add_data(self, TDH, CM, HC)
        self.driver.find_element_by_link_text('暂存').click()
        Test_report.compare_el(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '待发送新增-暂存')

    # 新增--待发送 > 发送
    def seed(self, TDH, CM, HC):
        """
        新增--待发送 > 发送
        :param TDH: 提单号
     :param CM: 船名
        :param HC: 航次
        :return:
        """
        self.driver.find_element_by_link_text('预配舱单申报').click()
        self.driver.find_element_by_link_text('申报预配舱单').click()
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(1)
        Test_report.add_data(self, TDH, CM, HC)
        self.driver.find_element_by_xpath('//*[@id="sendButton"]').click()
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button[2]').click()
        time.sleep(2)
        Test_report.compare_el(self, 'xpath', '/html/body/div[10]/div/div/div[1]/div', '成功', '待发送新增-发送')

    # 删除--待发送
    def rm_wait_seed(self):
        """删除--待发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"待发送").click()
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

    # 修改 ：暂存，发送-- 待发送
    def update_wait_seed(self, TDH, CM, HC):
        """修改 -- 待发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()

        driver.find_element_by_xpath(u"(//a[contains(text(),'修改')])[1]").click()
        num = str(random.randint(1, 1000))
        driver.find_element_by_id("BILL_NBR").send_keys(num)
        driver.find_element_by_link_text(u"暂存").click()
        # 判断是否提示成功
        Test_report.compare_el(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '成功', '待发送-修改-暂存')

        time.sleep(2)
        Test_report.add_box(self, TDH, CM, HC)
        self.driver.find_element_by_xpath('//*[@id="sendButton"]').click()
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button[2]').click()
        time.sleep(2)
        # 是否提示成功
        Test_report.compare_el(self, 'xpath', '/html/body/div[10]/div/div/div[1]/div', '成功', '待发送修改-发送')

    # Excel历史查看--待发送
    def excel_history(self):
        """Excel历史查看--待发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"Excel历史").click()
        time.sleep(2)
        driver.find_element_by_id("buttonCancelEditExcel").click()

    # 导入--待发送
    def import_excel(self):
        """导入--待发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"导入").click()
        time.sleep(2)
        os.system(r'D:\模板文件\test.exe "C:\Users\wh\Desktop\测试流程\EDI舱单模板.txt"')
        Test_report.el_show(self, 'xpath', '//*[@id="text-body"]/h3', '待发送-导入')

    # 批量发送-待发送
    def seed_more(self):
        """批量发送-待发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/thead/tr/th[1]/div/span/input').click()
        driver.find_element_by_link_text(u"批量发送").click()
        time.sleep(2)
        Test_report.el_show(self, 'xpath', '/html/body/div[7]/div/div/div[1]/div', '待发送-批量发送')

    # 修改--已发送  （暂存，重新发送）
    def update_seed(self):
        """修改--已发送  （暂存，重新发送）"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"修改").click()
        num = str(random.randint(1, 1000))
        print(num)
        self.el_show('xpath', '//*[@id="formDtl"]/div[2]/table/tbody/tr[1]/td[2]', '提单号')
        self.driver.find_element_by_xpath('//input[@name="FREIGHT_NBR"]').send_keys(num)
        driver.find_element_by_link_text(u"暂存").click()
        driver.find_element_by_css_selector("button.toast-close-button").click()
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '已发送-修改：暂存')

        driver.find_element_by_link_text(u"更改报文发送").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath("//i[@onclick='returnQuery()']").click()

    # 报文历史查看--已发送
    def report_history(self):
        """报文历史查看--已发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_xpath('//*[@id="content-main-section"]/div[3]/div/div/div/div/ul/li[2]/a').click()
        driver.find_element_by_link_text(u"报文历史").click()
        time.sleep(2)
        driver.find_element_by_id("buttonCancelEditEdi").click()

    # excel历史查看--已发送
    def excel_history_seed(self):
        """excel历史查看--已发送"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"Excel历史").click()
        time.sleep(2)
        driver.find_element_by_id("buttonCancelEditExcel").click()

    # 已发送-复制新增 添加数据
    def copy_add_data(self, TDH, CM, HC):
        """已发送-复制新增 添加数据"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_link_text(u"复制新增").click()
        time.sleep(1)
        driver.find_element_by_id("BILL_NBR").clear()
        driver.find_element_by_id("BILL_NBR").send_keys(TDH)
        driver.find_element_by_id("E_SHIP_NAM").clear()
        driver.find_element_by_id("E_SHIP_NAM").send_keys(CM)
        driver.find_element_by_id("OUT_VOYAGE_NO").clear()
        driver.find_element_by_id("OUT_VOYAGE_NO").send_keys(HC)
        target = driver.find_element_by_xpath(
            '//*[@id="text-body"]/div[2]/div[1]/a')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标拖动到可见的元素去

        # 货物信息新增

        driver.find_element_by_css_selector(
            '#text-body > div.body-div.portlet.light.bordered > div:nth-child(2) > a').click()
        driver.find_element_by_css_selector("div.col-md-8 > #PIECE_NUM").send_keys("220")
        driver.find_element_by_css_selector("div.col-md-8 > #GWEIGHT_TON").send_keys("220")
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#inputCargoDtl > div > div.modal-body > div > div > div:nth-child(6) > div > div > input").send_keys(
            "220")
        element = driver.find_element_by_xpath(
            "//form[@id='inputCargoDtl']/div/div/div/div/div[3]/div/div/span/input[2]")
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('Rod/RD')
        driver.find_element_by_css_selector("div.col-md-8 > #GVOL_NUM").send_keys("220")
        driver.find_element_by_css_selector(
            '#inputCargoDtl > div > div.modal-body > div > div > div:nth-child(8) > div > div > textarea').send_keys(
            'WU')
        time.sleep(2)
        driver.find_element_by_id("buttonInputCargoDtl").click()
        # add.cut_image('新增2')
        # png_num = random.randint(1, 100)
        # url = '../image/' + str(png_num) + '.png'
        # self.driver.get_screenshot_as_file(url)
        # print('新增截图2的编号是：%s' % png_num)

        el = (By.XPATH, '/html/body/div[8]/div/div/div[2]/button')
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(el))
            print('货物信息新增成功点击加载出来了')
        except:
            print('货物信息新增成功点击加载失败')

        driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/button").click()

        # 新增箱号集装箱细目
        el = (By.XPATH, '//*[@id="text-body"]/div[2]/div[2]/a')
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(el))
            print('箱号新增点击加载出来了')
        except:
            print('箱号新增点击加载失败')

        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="text-body"]/div[2]/div[2]/a').click()
        driver.find_element_by_css_selector('#inputCntrDtl > div:nth-child(1) > div > div > input').send_keys(
            "TEST1234568")  # 箱号
        element_03 = self.driver.find_element_by_xpath('//*[@id="CNTR_SIZE_COD"]')
        select_03 = Select(element_03)
        select_03.select_by_visible_text('20')  # 箱型
        element_03 = self.driver.find_element_by_xpath('// *[ @ id = "CNTR_TYPE_COD"]')
        select_03 = Select(element_03)
        select_03.select_by_visible_text('GP')  # 箱型

        driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(2) > div > div > input").send_keys(
            "220")  # 铅封号

        driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(4) > div > div > input").send_keys(
            "220")  # 件数

        driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(6) > div > div > input").send_keys(
            "220")  # 货内箱体积

        driver.find_element_by_css_selector("#inputCntrDtl > div:nth-child(5) > div > div > input").send_keys(
            "220")  # 货内货重

        Select(driver.find_element_by_xpath("//div[7]/div/div/select")).select_by_visible_text(u"整箱")
        # Select(driver.find_element_by_id("CNTR_TYPE_COD")).select_by_visible_text("BK")
        Select(driver.find_element_by_id("SOC_ID")).select_by_visible_text(u"货主箱")

        time.sleep(2)
        # 点击保存新增箱号
        driver.find_element_by_id("buttonInputCntrDtl").click()  # /html/body/div[10]/div/div/div[2]/button

        time.sleep(1)
        # 点击箱号新增操作成功
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button').click()

        #  总件毛体
        el = (By.XPATH, '//*[@id="PIECE_NUM"]')
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(el))
            print('总件毛体点击加载出来了')
        except Exception as e:
            print('总件毛体点击加载失败', e)
        driver.find_element_by_xpath(
            "//*[@id='PIECE_NUM']").send_keys('220')

        driver.find_element_by_xpath(
            '//*[@id="GWEIGHT_TON"]').send_keys(
            '220')
        driver.find_element_by_xpath(
            '//*[@id="GVOL_NUM"]').send_keys(
            '220')
        time.sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="GWEIGHT_TON"]').click()
        # 点击发送
        target = driver.find_element_by_xpath(
            '//*[@id="sendButton"]')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标下拉框向上移动

    # 复制新增--已发送 > 暂存
    def copy_add01(self, TDH, CM, HC):
        """
        复制新增--已发送 > 暂存
        TDH = 提单号； CM = 船名；   HC = 航次
        :return:
        """
        Test_report.copy_add_data(self, TDH, CM, HC)
        self.driver.find_element_by_link_text('暂存').click()
        time.sleep(2)
        Test_report.el_show(self, 'xpath', '//*[@id="toast-container"]/div/div[2]', '已发送-复制新增：暂存')

    # 复制新增--已发送 > 发送
    def copy_add03(self, TDH, CM, HC):
        """
        复制新增--已发送 > 发送
        TDH = 提单号； CM = 船名；   HC = 航次
        :return:
        """
        Test_report.copy_add_data(self, TDH, CM, HC)
        self.driver.find_element_by_xpath('//*[@id="sendButton"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/button[2]').click()
        Test_report.el_show(self, 'xpath', '/html/body/div[10]/div/div/div[1]/div', '待发送修改-发送')

    # 查询-重置-已发送清单导出--已发送
    def select_seed(self, TDH, YBH, CM, HC):
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text(u"已发送").click()
        driver.find_element_by_name("billnbr").send_keys(TDH)
        driver.find_element_by_name("freightnbr").send_keys(YBH)
        driver.find_element_by_name("shipnam").send_keys(CM)
        driver.find_element_by_name("voyageno").send_keys(HC)
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath(
            '//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div/div/div/div/div[3]/div/a[2]').click()
        driver.find_element_by_link_text('已发送清单导出').click()

    # 导入EDI舱单报文
    def import_edi(self):
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text('导入EDI舱单报文').click()
        driver.find_element_by_xpath('//*[@id="content-main-section"]/div[3]/div/div/div/div/div/div[1]/div/a').click()
        os.system(r'D:\模板文件\test.exe "C:\Users\wh\Desktop\测试流程\EDI舱单模板.txt"')
        time.sleep(2)
        Test_report.el_show(self, 'xpath', '//*[@id="uploadEdiInfo"]/div/table/thead/tr/th[2]', '导入EDI舱单报文')

    # EDI解析记录
    def record_edi(self):
        """# EDI解析记录"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text('EDI解析记录').click()
        # driver.find_element_by_xpath('//*[@id="from"]').click()
        js = 'document.getElementById("from").value = "2019-08-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        # 判断查询结果是否成功
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/thead/tr/th[6]')
        driver.find_element_by_link_text('重置').click()
        time.sleep(2)

    # 代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回
    def manifest_management(self):
        """ 代发舱单管理--待处理--查询 > 查看 > 报文历史 > 已处理 > 撤回"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text('代发舱单管理').click()
        driver.find_element_by_link_text('待处理').click()
        js = 'document.getElementById("from").value = "2018-08-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[5]')

        # 查看
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[1]', '查看')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[1]').click()
        self.el_show('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', 'xx')
        time.sleep(2)
        self.get_length('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]')
        time.sleep(2)

        driver.find_element_by_css_selector('#close > .fa').click()

        # 报文历史
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[2]', '报文历史')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[2]').click()
        self.el_show('text', '取消', '取消点击')
        driver.find_element_by_link_text('取消').click()
        time.sleep(2)

        # 已处理
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[3]', '报文历史')
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/button[2]').click()
        # 撤回
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[4]', '撤回')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[12]/a[4]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="message"]').send_keys('111')
        self.el_show('text', '确认', '确认点击')
        driver.find_element_by_link_text('确认').click()

    # 代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息
    def manifest_management01(self):
        """代发舱单管理--已处理--查询 > 查看 > 报文历史 > 改单信息"""
        driver = self.driver
        driver.find_element_by_link_text(u"预配舱单申报").click()
        driver.find_element_by_link_text('代发舱单管理').click()
        driver.find_element_by_link_text('已处理').click()
        js = 'document.getElementById("from").value = "2018-8-06"'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_link_text('查询').click()
        Test_report.get_length(self, 'xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[5]')

        # 查看
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[1]').click()
        self.el_show('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]', 'xx')
        time.sleep(2)
        self.get_length('xpath', '//*[@id="text-body"]/div/div[2]/table/tbody/tr[1]/td[2]')
        time.sleep(2)
        driver.find_element_by_css_selector('#close > .fa').click()

        # 报文历史
        self.el_show('xpath', '//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[2]', '报文历史')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="purchaseOrdersearchTable"]/tbody/tr[1]/td[13]/a[2]').click()
        self.el_show('text', '取消', '取消点击')
        driver.find_element_by_link_text('取消').click()


    # 港口代码参照表下载，舱单模板下载
    def down_db(self):
        """港口代码参照表下载，舱单模板下载"""
        driver = self.driver
        driver.find_element_by_link_text('预配舱单申报').click()
        driver.find_element_by_link_text('舱单模板下载').click()
        driver.find_element_by_link_text('港口代码参照表').click()
        time.sleep(2)
