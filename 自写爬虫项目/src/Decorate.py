#--* coding=utf-8 *--

"""
    程序说明文档
    这是一个装修工程类，包含装修工程的数据传输和获取方法，封装提交的Request数据，只需调用方法即可获取

    编写者：Zion
    编写日期：2021年1月26日15:43:16
    增加功能：增加装修工程厂商类，添加协议头,获取
"""
import requests as req
from src.Manufature import Manufature
import json
from src.Enum_ID import *

class Decorate(Manufature):
    """
    装修工程厂商
    """
    def __init__(self):
        #调用父类方法
        super(Decorate, self).__init__()
        #修改装修工程类的协议头
        self.setReferer(Enum_Referer.Decorate)
        #修改装修工程类的提交数据
        self.data.setGoodsClassGuid(Enum_ClassGuid.Decorate)

        self.filename = "装修服务"






if __name__ == "__main__":
    pass
