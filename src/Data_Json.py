# --* coding="utf-8" *--

import json


# 这是一个数据类型，用于提交POST信息
class Data_Json:
    def __init__(self, data=dict()):
        self.data = dict()
        self.data["pageNumber"] = 1
        self.data["pageSize"] = 10
        self.data["sortType"] = 0
        self.data["sortOrder"] = "asc"
        self.data["goodsClassGuid"] = "ff80808174c46e510174c49e58c60033"
        self.data["addressid"] = ""

    def setPageSize(self, pagesize):
        """
         修改每页数据条数量
        :param pagesize:当前页数量，默认10条
        :return: None
        """
        self.data.update(pageSize=pagesize)

    def setPageNumber(self, pagenumber):
        """
        修改获取页数
        :param pagenumber: 修改获取页数，默认获取第1页的数据
        :return: None
        """
        self.data.update(pageNumber=pagenumber)

    def setGoodsClassGuid(self, goods_class_guid):
        """
        修改获取厂家的页面
        :param goods_class_guid:根据提交不同的Guid，获取不同厂商的连接
        :return: None
        """
        self.data.update(goodsClassGuid=goods_class_guid)

    def getJson(self):
        """
        返回Json格式
        :return: Json
        """
        return self.data

    def getLength(self):
        return len(str(json.dumps(self.data)).replace(" ", ""))
