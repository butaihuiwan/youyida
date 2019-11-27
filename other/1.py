import time

from selenium import webdriver


def baidu():
    print(1)
    opt = webdriver.ChromeOptions()
    opt.headless = True
    opt.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(options=opt)
    driver.get('http://192.168.17.50:2090/home/control/main')
    driver.find_element_by_name('USERNAME').send_keys('customer1')
    driver.find_element_by_name('PASSWORD').send_keys('123456')
    time.sleep(1)
    login = driver.find_element_by_xpath('/html/body/div[3]/form/div[5]/button[1]')
    login.click()
    time.sleep(3)
    driver.maximize_window()
