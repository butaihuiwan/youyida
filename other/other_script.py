import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .Commonlib import Commonshare


class Data(Commonshare):
    """舱单数据"""

    # def __init__(self, driver):
    #     driver = self.driver

    def data_clear(self, TDH, CM, HC):
        """修改清空舱单数据"""
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
        self.driver.find_element_by_id('BILL_NBR').clear()

        self.driver.find_element_by_id('E_SHIP_NAM').clear()

        self.driver.find_element_by_id('OUT_VOYAGE_NO').clear()

        # self.driver.find_element_by_id('TRUST_INFO').clear()
        self.rm_imput('id', 'TRUST_INFO')

        self.driver.find_element_by_name('FREIGHT_NBR').clear()

        self.driver.find_element_by_name('BILL_ORIG_NUM').clear()

        self.driver.find_element_by_name('MASTER_NO').clear()

        # 发货人信息
        self.driver.find_element_by_id('SHIPPER_COD').clear()

        self.driver.find_element_by_id('E_SHIPPER_NAM').clear()

        time.sleep(1)

        self.rm_imput('id', 'SHIPPER_COUNTRY_COD')

        self.driver.find_element_by_id('SHIPPER_ADD_STR').clear()

        self.driver.find_element_by_id('SHIPPER_TE_STR').clear()

        self.driver.find_element_by_id('SHIPPER_EM_STR').clear()

        self.driver.find_element_by_id('SHIPPER_FX_STR').clear()

        # 收货人信息
        self.driver.find_element_by_id('CONSIGNEE_COD').clear()

        self.driver.find_element_by_id('E_CONSIGNEE_NAM').clear()

        self.rm_imput('id', 'CONSIGNEE_COUNTRY_COD')

        self.rm_imput('name', 'CONSIGNEE_ADD_STR')

        self.driver.find_element_by_id('CONSIGNEE_TE_STR').clear()

        self.driver.find_element_by_id('CONSIGNEE_EM_STR').clear()

        self.driver.find_element_by_id('SHIPPER_FX_STR').clear()

        self.driver.find_element_by_id('CONSIGNEE_CONTACT_NAM').clear()

        self.rm_imput('id', 'CONSIGNEE_CONTACT_TE_STR')

        self.driver.find_element_by_id('CONSIGNEE_CONTACT_EM_STR').clear()

        self.driver.find_element_by_id('CONSIGNEE_CONTACT_FX_STR').clear()

        self.rm_imput('name', 'CONSIGNEE_AEO')

        # 通知人信息
        self.driver.find_element_by_id('NOTIFY_COD').clear()

        self.driver.find_element_by_id('E_NOTIFY_NAM').clear()

        self.rm_imput('id', 'NOTIFY_COUNTRY_COD')
        self.rm_imput('name', 'NOTIFY_ADD_STR')
        self.driver.find_element_by_id('NOTIFY_TE_STR').clear()

        self.driver.find_element_by_id('NOTIFY_EM_STR').clear()

        self.driver.find_element_by_id('NOTIFY_FX_STR').clear()

        # 地点信息
        self.rm_imput('name', 'START_PORT_NAM')

        self.rm_imput('name', 'LOAD_PORT_FULLNAM')

        self.rm_imput('name', 'DISCHRG_PORT_FULLNAM')

        self.rm_imput('name', 'TRANS_PORT_FULLNAM')

        self.rm_imput('name', 'DEST_PORT_FULLNAM')

        driver = self.driver
        time.sleep(1)
        target = driver.find_element_by_xpath(
            '//*[@id="text-body"]/div[2]/div[1]/a')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 鼠标拖动到可见的元素去

        """清空舱单箱子，货物信息"""
        try:
            driver.find_element_by_xpath('(//a[contains(@href, "javascript:;")])[12]').click()
            driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button[2]').click()
            driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button').click()
        except Exception as e:
            print('货物信息pass')
        try:
            el = driver.find_element_by_xpath(' //a[contains(@href, "javascript:;")])[14]').click()
            driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/button[2]').click()
            driver.find_element_by_xpath('//button[@type="button"])[4]').click()
        except Exception as e:
            print('箱号pass')

        """清空舱单总件毛体数据"""
        el = (By.XPATH, '//*[@id="PIECE_NUM"]')
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(el))
            print('总件毛体点击加载出来了')
            self.el_show('xpath', '//*[@id="PIECE_NUM"]', '总数量')
            self.rm_imput('xpath', '//*[@id="PIECE_NUM"]')

            self.el_show('xpath', '//*[@id="GWEIGHT_TON"]', '总数量')
            self.rm_imput('xpath', '//*[@id="GWEIGHT_TON"]')

            self.el_show('xpath', '//*[@id="GVOL_NUM"]', '总数量')
            self.rm_imput('xpath', '//*[@id="GVOL_NUM"]')
        except Exception as e:
            print('总件毛体点击加载失败', e)

    def add_data(self, seed, TDH, CM, HC):
        """新增填写的数据"""

        # 选择发送人代码
        element = self.driver.find_element_by_id('BILL_SENDER_CODE')
        select = Select(element)
        select.select_by_visible_text(seed)
        time.sleep(1)
        # self.driver.implicitly_wait(10)

        # 选择接受人代码
        element = self.driver.find_element_by_id('BILL_RECEIVER_CODE')
        select = Select(element)
        select.select_by_visible_text('民生船代')

        # 订舱信息
        self.driver.find_element_by_id('BILL_NBR').send_keys(TDH)
        self.driver.find_element_by_id('E_SHIP_NAM').send_keys(CM)
        self.driver.find_element_by_id('OUT_VOYAGE_NO').send_keys(HC)
        self.driver.find_element_by_id('TRUST_INFO').send_keys('YML：阳明')
        element_03 = self.driver.find_element_by_id('TYPE_OF_BILL')
        select_03 = Select(element_03)
        select_03.select_by_visible_text('WAYBILL')
        element_04 = self.driver.find_element_by_id('PAY_WAY_ID')
        select_04 = Select(element_04)
        select_04.select_by_visible_text('到付')
        self.driver.find_element_by_name('FREIGHT_NBR').send_keys('TEST20191022')
        element_04 = self.driver.find_element_by_id('DR_TYPE_STR')
        select_04 = Select(element_04)
        select_04.select_by_visible_text('CY-FOR')
        self.driver.find_element_by_name('BILL_ORIG_NUM').send_keys('1')
        self.driver.find_element_by_name('MASTER_NO').send_keys('TEST20191022')

        # 发货人信息
        self.driver.find_element_by_id('SHIPPER_COD').send_keys('USCI+91320412MA1MGBN10R')
        self.driver.find_element_by_id('E_SHIPPER_NAM').send_keys('CHANGZHOU JIANKAI WOOD CO.,LTD')
        self.driver.find_element_by_id('SHIPPER_COUNTRY_COD').send_keys('CN')
        self.driver.find_element_by_id('SHIPPER_ADD_STR').send_keys(
            'NO.89,WEIFU ROAD,CUIQIAO,HENGLIN TOWN,WUJIN DISTRICT,CHANGZHOU CITY,JI')
        self.driver.find_element_by_id('SHIPPER_TE_STR').send_keys('0519-85189799')
        self.driver.find_element_by_id('SHIPPER_EM_STR').send_keys('1234567789@qq.com')
        self.driver.find_element_by_id('SHIPPER_FX_STR').send_keys('123456')
        self.driver.find_element_by_name('CONSIGNEE_AEO').send_keys('SH')

        # 收货人信息
        self.driver.find_element_by_id('CONSIGNEE_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
        self.driver.find_element_by_id('E_CONSIGNEE_NAM').send_keys('TOUCH EXPERTS GENERAL TRADING CO.,LTD')
        self.driver.find_element_by_id('CONSIGNEE_COUNTRY_COD').send_keys('IQ')
        self.driver.find_element_by_name('CONSIGNEE_ADD_STR').send_keys('IRAQ BAGHDAD VICTORY SQUAE')
        self.driver.find_element_by_id('CONSIGNEE_TE_STR').send_keys('123456789')
        self.driver.find_element_by_id('CONSIGNEE_EM_STR').send_keys('123456789@163.COM')
        self.driver.find_element_by_id('SHIPPER_FX_STR').send_keys('123456789')
        self.driver.find_element_by_id('CONSIGNEE_CONTACT_NAM').send_keys('BJ')
        # self.driver.find_element_by_id('CONSIGNEE_CONTACT_TE_STR').send_keys('12345678')
        self.driver.find_element_by_id('CONSIGNEE_CONTACT_EM_STR').send_keys('12345678@qq.com')
        self.driver.find_element_by_id('CONSIGNEE_CONTACT_FX_STR').send_keys('12345678')
        # self.driver.find_element_by_name('CONSIGNEE_AEO').send_keys('BJ')

        # 通知人信息
        self.driver.find_element_by_id('NOTIFY_COD').send_keys('CHAMBER OF COMMERCE NUMBER+198326691502')
        self.driver.find_element_by_id('E_NOTIFY_NAM').send_keys('TOUCH EXPERTS GENERAL TRADING CO.,LTD')
        self.driver.find_element_by_id('NOTIFY_COUNTRY_COD').send_keys('IQ')
        self.driver.find_element_by_name('NOTIFY_ADD_STR').send_keys('IRAQ BAGHDAD VICTORY SQUAE')
        self.driver.find_element_by_id('NOTIFY_TE_STR').send_keys('123456')
        self.driver.find_element_by_id('NOTIFY_EM_STR').send_keys('123456@qq.com')
        self.driver.find_element_by_id('NOTIFY_FX_STR').send_keys('1132123')

        # 地点信息
        self.driver.find_element_by_name('START_PORT_NAM').send_keys('ADA')
        self.driver.find_element_by_xpath(
            '//*[@id="formDtl"]/div[6]/table/tbody/tr[1]/td[2]/div[1]/span/div/div/div[1]').click()

        self.driver.find_element_by_name('LOAD_PORT_FULLNAM').send_keys('as')
        self.driver.find_element_by_xpath(
            '//*[@id="formDtl"]/div[6]/table/tbody/tr[1]/td[4]/div[1]/span/div/div/div[2]').click()
        self.driver.find_element_by_name('DISCHRG_PORT_FULLNAM').send_keys('BS')
        self.driver.find_element_by_xpath(
            '//*[@id="formDtl"]/div[6]/table/tbody/tr[2]/td[2]/div[1]/span/div/div/div[3]').click()
        self.driver.find_element_by_name('TRANS_PORT_FULLNAM').send_keys('CC')
        self.driver.find_element_by_xpath(
            '//*[@id="formDtl"]/div[6]/table/tbody/tr[2]/td[4]/div[1]/span/div/div/div').click()
        self.driver.find_element_by_name('DEST_PORT_FULLNAM').send_keys('ss')
        self.driver.find_element_by_xpath(
            '//*[@id="formDtl"]/div[6]/table/tbody/tr[3]/td[2]/div[1]/span/div/div/div').click()

        time.sleep(1)
        driver = self.driver

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
        self.el_show('xpath', '/html/body/div[8]/div/div/div[2]/button', '货物信息新增成功点击加载')
        driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/button").click()

        # 新增箱号集装箱细目
        self.el_show('xpath', '//*[@id="text-body"]/div[2]/div[2]/a', '箱号新增点击加载')
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
