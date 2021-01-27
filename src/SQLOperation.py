#--* coding = utf-8 *--

"""
    将JSON本地文件读取，并保存到MongoDB数据库中
    基本功能：数据库增删改查

    编写人：Zion
    编写时间：2021年1月27日11:19:38
    编写内容：
"""
import json
from src.PrintingService import *
import pymongo
import os
class SQLOperation:
    """
    数据库操作，将本地JSON文件保存到数据库，并更新
    父类
    """

    def __init__(self,sql_name,sql_path=""):
        self.createData()
        if self.sql_path != "":
            self.sql_path = sql_path
        else:
            self.sql_path = "..\\data\\"
        self.sql_path +=sql_name
        print(self.sql_path)
    def loadSQL(self):
        if not os.path.exists(self.sql_path):
            #如果没有找到数据库文件，则返回None
            return None
        else:
            pymongo.MongoClient("mongodb://localhost:27017/")
    def createSQL(self):
        """
        创建新的数据库
        :return:
        """
        pass


class ReadJson:
    """
    读取本地JSON文件
    """
    def loadJson(js_path):
        with open(js_path,"r",encoding="utf-8") as j:

            return json.load(j)




if __name__ == "__main__":
    xs_dict = ReadJson.loadJson("..\\data\\修缮工程.json")
    print(len(xs_dict["data"]["rows"]))
    for data in xs_dict["data"]["rows"]:
        print("""
        类型：{lx}
        
        联系人：{lxr}
        """.format(lx=data["goodsClassName"],lxr=data["linkMan"]))

