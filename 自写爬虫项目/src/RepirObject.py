#--* coding=utf-8 *--
"""
    这是修缮工程类

    编写人：Zion
    编写时间：2021年1月26日17:32:20
    增加内容：修缮工程类初始化
"""

from src.Manufature import Manufature
from src.Enum_ID import *
from src.Manufature import *
class RepirObject(Manufature):
    """
    修缮工程类
    """
    def __init__(self):
        #调用父类初始化防范
        super(RepirObject, self).__init__()
        #修改修缮工程引用页
        #self.headers.update(Enum_Referer.Repir_object)
        self.setReferer(Enum_Referer.Repir_object)
        #修改修缮工程提交数据
        #self.data.setGoodsClassGuid(Enum_ClassGuid.Repir_object)
        self.data.setGoodsClassGuid(Enum_ClassGuid.Repir_object)

        #修改类保存名
        self.filename = "修缮工程"


