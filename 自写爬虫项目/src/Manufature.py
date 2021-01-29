#--* coding=utf-8 *--
"""
    * 说明文档
    * 这是一个厂商类
    * 所有子类必须继承厂商类，方便多态
    *
    * 编写者：Zion
    * 编写时间：2021年1月26日15:11:15
    * 增加功能：创建厂商类，使子类继承厂商，方便底层代码维护
"""

from 自写爬虫项目.src.Data_Json import Data_Json
import requests as req
from src.Enum_ID import *

MAX = 10000

#父类：厂商类，所有子类厂商必须继承父类
class Manufature:
    def __init__(self):

        #添加数据类
        self.data = Data_Json()

        #初始化协议头字典
        self.headers = {
            "Host": "gdgpo.czt.gd.gov.cn",
            "Connection": "keep-alive",
            "Content-Length": str(self.data.getLength()),
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://gdgpo.czt.gd.gov.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
            "Referer":Enum_Referer.Decorate
        }
        #提交地址
        self.post_url = "https://gdgpo.czt.gd.gov.cn/gateway/gp-provide/api/v2/searchProvideSortInformation"
        #类保存名
        self.filename = "Manufature"


    def setHost(self,host):
        """
        设置Host
        :param host: 新的Host
        :return: None
        """
        self.headers.update({"Host" : host})

    def __setContent_Length(self,length):
        """
        修改提交数据字节长度
        :param length: 新的数据长度，使用Data_Json.getLength()获取
        :return: Int型
        """
        self.headers.update({"Content-Length" : str(length)})

    def setUserAgent(self,user_agent):
        """
        修改提交网页访问代理
        :param user_agent: 新的访问代理
        :return:None
        """
        self.headers.update({"User-Agent":user_agent})

    def setReferer(self,referers):
        """
        设置引用页，根据不同的环境设置
        :param referers:使用Enum_ClassGuid模块导入
        :return:None
        """
        self.headers.update({"Referer":referers})

    def getDataJson(self,page=10):
        """
        获取厂商数据
        :return: 返回Json文本
        """
        try:
            self.data.setPageSize(page)
            self.respon = req.post(url=self.post_url,headers = self.headers,json=self.data.getJson())
            return (self.respon.text,"{name}获取成功!".format(name = self.filename))
        except(Exception) as ex:
            print("{name} 访问数据页面错误，错误信息：{ex}".format(name = self.filename,ex = ex))
            #return (None,"{name}获取失败".format(name = self.filename))
    def SaveData(self):
        """
        保存到本地文件
        :return: None
        """
        path = "..\data\\{name}.json".format(name = self.filename)
        try:
            with open(path,"wt",encoding="utf-8") as js:
                js.write(self.respon.text)

                print("{name} 保存成功!".format(name = self.filename))
        except(Exception) as ex:
            print("{name} 保存错误！请检查\n 错误信息：{ex}".format(name= self.filename,ex = ex))

