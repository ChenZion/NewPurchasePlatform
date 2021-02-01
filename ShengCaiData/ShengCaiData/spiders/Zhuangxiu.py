'''
Author: your name
Date: 2021-01-29 14:14:32
LastEditTime: 2021-01-29 14:22:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \ShengCaiData\ShengCaiData\spiders\Zhuangxiu.py
'''
import scrapy
import json
from .publicCode.Submit import *
from ShengCaiData.ShengCaiData.items import ShengcaidataItem

class ZhuangxiuSpider(scrapy.Spider):
    name = 'Zhuangxiu'
    zx_items = ShengcaidataItem()


    def start_requests(self):
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
            "Connection": "keep-alive",
            #"Content-Length": "128",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "gdgpo.czt.gd.gov.cn",
            "Origin": "https://gdgpo.czt.gd.gov.cn",
            "Referer": "https://gdgpo.czt.gd.gov.cn/provide/list/ff80808174c46e510174c49e58c60033/%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B?source=31",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }

        header1 = {
            "Host": "gdgpo.czt.gd.gov.cn",
            "Connection": "keep-alive",
            # "Content-Length": "134",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://gdgpo.czt.gd.gov.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://gdgpo.czt.gd.gov.cn/provide/list/ff80808174c46e510174c49e58c60033/%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B?source=31",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "regioncode=440001; regionname=5bm/5Lic55yB5pys57qn; regionguid=2137001; regioncode=440001"
        }
        return [scrapy.Request(url= START_POST_URL,method="POST",headers=header,body=Request_Data(enum_guid=Enum_GoodsClassGuid.zhuangxiu_guid,pagesize=10000).__str__(),callback=self.parse)]



    def parse(self, response):
        sc_items = ShengcaidataItem()
        js = json.loads( response.body.decode("UTF-8"))
        for info in js["data"]["rows"]:
            item[·]


    def getDataParse(self,response):

