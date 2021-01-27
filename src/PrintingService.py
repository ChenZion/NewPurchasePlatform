#--* ciding=utf-8 *--
"""
    这是印刷服务类

    编写人：Zion
    编写时间：2021年1月26日19:36:40
    编写功能：增加印刷服务类，获取印刷数据功能

"""

from src.Manufature import Manufature
from src.Enum_ID import *

class PrintingService(Manufature):
    """
    印刷服务类
    """
    def __init__(self):
        """
        印刷服务类初始化方法
        """
        #调用父类通用初始化方法
        super(PrintingService, self).__init__()
        #修改印刷服务类的代理页
        self.setReferer(Enum_Referer.Printing_service)
        #修改印刷服务类的提交数据
        self.data.setGoodsClassGuid(Enum_ClassGuid.Printing_service)

        self.filename = "印刷服务"

