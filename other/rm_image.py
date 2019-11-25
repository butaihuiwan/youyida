import os
import shutil


def rm_image():
    try:
        url = shutil.rmtree(r'C:\Users\wh\PycharmProjects\youyida\suit\image')
        print('imgae文件夹删除完成')
    except:
        print('文件不存在')

    # 新建image 文件夹
    os.mkdir(r'C:\Users\wh\PycharmProjects\youyida\suit\image')


def rm_report():
    try:
        url = shutil.rmtree(r'C:\Users\wh\PycharmProjects\youyida\report')
        print('report文件夹删除完成')
    except:
        print('文件不存在')

    # 新建image 文件夹
    os.mkdir(r'C:\Users\wh\PycharmProjects\youyida\report')
