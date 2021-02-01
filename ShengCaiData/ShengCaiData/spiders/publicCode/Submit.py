# -*- coding:utf-8 -*-
'''
Author: your name
Date: 2021-01-29 14:17:48
LastEditTime: 2021-01-29 17:48:59
LastEditors: Please set LastEditors
Description: 这是一个爬虫公共类，编写提交的公共信息，enum类型等，方便爬虫提交减少重复代码
FilePath: \ShengCaiData\ShengCaiData\spiders\publicCode\Submit.py
'''

START_POST_URL = "https://gdgpo.czt.gd.gov.cn/gateway/gp-provide/api/v2/searchProvideSortInformation"


class Enum_GoodsClassGuid:
    """
    顶点集市类型GUID
    """
    zhuangxiu_guid = "ff80808174c46e510174c49e58c60033"  # 装修工程
    xiushan_guid = "ff80808174c46e510174c4af0cd70044"  # 修缮服务
    hulianwangjieru_guid = "ff80808174c46e510174c4af78a50046"  # 互联网接入电信增值服务
    yinshua_guid = "ff80808174c46e510174c4b0da8e004c"  # 印刷服务


class Enum_Referer:
    """
    引用页的枚举类，不同的类型
    """
    zhuangxiu_ref = "https://gdgpo.czt.gd.gov.cn/provide/list/" + Enum_GoodsClassGuid.zhuangxiu_guid + "/%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B?source=31"
    xiushan_ref = "https://gdgpo.czt.gd.gov.cn/provide/list/" + Enum_GoodsClassGuid.xiushan_guid + "/%E4%BF%AE%E7%BC%AE%E5%B7%A5%E7%A8%8B?source=31"
    hulianwangjieru_ref = "https://gdgpo.czt.gd.gov.cn/provide/list/" + Enum_GoodsClassGuid.hulianwangjieru_guid + "/%E4%BA%92%E8%81%94%E7%BD%91%E6%8E%A5%E5%85%A5%E6%9C%8D%E5%8A%A1?source=31"
    yinshua_ref = "https://gdgpo.czt.gd.gov.cn/provide/list/" + Enum_GoodsClassGuid.yinshua_guid + "/%E5%8D%B0%E5%88%B7%E6%9C%8D%E5%8A%A1?source=31"


class Request_Header:
    """根据输入返回不同类型的请求头"""

    def __init__(self, enum_referer):
        """
        初始化提交头
        enum_referer:项目的初始化
        """
        self.headers = {
            "Host": "gdgpo.czt.gd.gov.cn",
            "Connection": "keep-alive",
            # "Content-Length": str(data_len),
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://gdgpo.czt.gd.gov.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
            "Referer": enum_referer
        }

    def __dict__(self):
        return self.headers

    def __str__(self):
        return str(self.headers).replace(" ", "")

    def __len__(self):
        return len(self.__str__())

    def __getitem__(self, item):
        return self.headers[item]


class Request_Data():
    """
    提交数据的字典
    """

    def __init__(self, enum_guid, pagesize='10'):
        self.data_str = """{{"pageNumber":"1","pageSize":\"{0}\","sortType":"0","sortOrder":"asc","goodsClassGuid":\"{1}\","addressid":""}}""".format(
            pagesize, enum_guid)

    def __str__(self):
        return self.data_str

    def __len__(self):
        return len(self.data_str)


if __name__ == "__main__":
    print(Request_Data(Enum_GoodsClassGuid.zhuangxiu_guid,"1000").__str__())
