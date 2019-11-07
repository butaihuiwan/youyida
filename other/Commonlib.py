import random
import re

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from unittest import TestCase
import unittest
from selenium.webdriver.common.by import By


class Commonshare(object):

    def __init__(self):
        """初始化方法,创建浏览器对象"""

        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(2)

    def rm_imput(self, locate_type, value):
        """清空指定元素输入框中内容"""
        el = self.locateElement(locate_type, value)
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.BACKSPACE)

    def locateElement(self, locate_type, value):
        """判断定位方式并调用相关方法"""

        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        # 如果el不为None,则返回
        if el is not None:
            return el

    def click(self, locate_type, value):
        """指定对某一元素的点击操作"""
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()
        time.sleep(1)

    def input_data(self, locate_type, value, data):
        """ # 对指定的元素进行数据输入"""
        el = self.locateElement(locate_type, value)
        # 执行输入操作
        el.send_keys(data)

    def get_text(self, locate_type, value):
        """获取指定元素的文本内容"""
        el = self.locateElement(locate_type, value)
        return el.text

    def get_attr(self, locate_type, value, data):
        """ 获取指定元素的属性值"""
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)

    def compare_el(self, locate_type, value, data_value, ex):
        """断言：是否相同
        locate_type：定位方式
        value: 定位表达式
        data_value: 匹配值
        ex：标题
        """
        data_get = Commonshare.get_text(self, locate_type, value)
        print(data_get)

        if re.search(data_get, data_value):
            print('%s ok' % ex)
        else:
            print('%s error' % ex)
            assert (1 == 2)

    def el_show(self, locate_type, value, ex):
        """判断输入的元素是否加载成功"""
        el = None
        if locate_type == 'id':
            el = (By.ID, value)
        elif locate_type == 'name':
            el = (By.NAME, value)
        elif locate_type == 'css':
            el = (By.CSS_SELECTOR, value)
        elif locate_type == 'text':
            el = (By.LINK_TEXT, value)
        elif locate_type == 'xpath':
            el = (By.XPATH, value)
        elif locate_type == 'class':
            el = (By.CLASS_NAME, value)
        elif locate_type == 'partial link text':
            el = (By.PARTIAL_LINK_TEXT, value)
        elif locate_type == 'tag':
            el = (By.TAG_NAME, value)

        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(el))
            print('%s:ok' % ex)
        except Exception as e:
            print('error_错误：%s' % ex)
            return False

    def get_length(self, locate_type, value):
        """判断查询结果是否成功"""
        text = Commonshare.get_text(self, locate_type, value)
        print(text)
        num = len(text)

        assert (0 != num)
        print('ok')

    def save_img(self, img_name):
        """截图"""
        self.driver.get_screenshot_as_file(r'C:\Users\wh\PycharmProjects\untitled\suit\image\%s' % img_name)

    # 收尾清理方法
    def __del__(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    pass
