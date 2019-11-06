import random
import re

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from unittest import TestCase
import unittest
from selenium.webdriver.common.by import By


class Commonshare(object):

    # 初始化方法
    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(2)

    def locateElement(self, locate_type, value):
        # 判断定位方式并调用相关方法

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

    # 指定对某一元素的点击操作
    def click(self, locate_type, value):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()
        time.sleep(1)

    # 对指定的元素进行数据输入
    def input_data(self, locate_type, value, data):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        # 执行输入操作
        el.send_keys(data)

    # 获取指定元素的文本内容
    def get_text(self, locate_type, value):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        return el.text

    # 获取指定元素的属性值
    def get_attr(self, locate_type, value, data):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)

    # 截图
    def cut_image(self, image):
        png_num = random.randint(1, 100)
        print('%s截图的编号是：%s ' % (image, png_num))
        url = '../image/' + str(png_num) + '.png'
        self.driver.get_screenshot_as_file(url)

    # 断言，输入输出是否相同
    def compare_el(self, locate_type, value, data_value, ex):
        """断言：是否相同
        locate_type：定位方式
        value: 定位表达式
        data_value: 匹配值
        ex：标题
        """
        data_get = Commonshare.get_text(self, locate_type, value)
        print(data_get)

        if re.search(data_value, data_get):
            print('%s ok' % ex)
        else:
            print('%s error' % ex)

    # 判断输入的元素是否加载成功
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

    def get_length(self, locate_type, value):
        """判断查询结果是否成功"""
        text = Commonshare.get_text(self, locate_type, value)
        print(text)
        num = len(text)
        try:
            assert (0 != num)
            print('ok')
        except Exception as e:
            print('error_错误：%s' % e)

    def get_img(self, img_name):
        self.driver.get_screenshot_as_file(r'C:\Users\wh\PycharmProjects\untitled\suit\image\%s' % img_name)

    # 收尾清理方法
    def __del__(self):
        time.sleep(1)
        self.driver.close()


if __name__ == '__main__':
    pass
