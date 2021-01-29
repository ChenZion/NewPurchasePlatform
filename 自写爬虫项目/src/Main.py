#--* coding=utf-8 *--/

from 自写爬虫项目.src.Decorate import Decorate
from 自写爬虫项目.src.PrintingService import PrintingService
from src.RepirObject import *
def Main():
    pass

def getAllJson():
    """
    获取所有页面的全部数据，并覆盖本地JSON文件
    :return: None
    """
    # 实例化对象
    decorate = Decorate()  # 装修工程
    printing = PrintingService()  # 印刷服务
    repir = RepirObject()  # 修缮工程

    # 获取修缮工程数据并保存本地
    repir.getDataJson(10000)
    repir.SaveData()

    # 获取装修工程数据并保存本地
    # decorate.getDataJson(10000)
    # decorate.SaveData()
    # # 获取印刷服务并保存本地
    # printing.getDataJson(1000)
    # printing.SaveData()



if __name__ == "__main__":
    getAllJson()

