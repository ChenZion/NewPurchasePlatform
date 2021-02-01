'''
Author: your name
Date: 2021-01-29 11:26:12
LastEditTime: 2021-01-29 11:45:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
'''
import scrapy


class TesttestSpider(scrapy.Spider):
    name = 'testtest'
    #allowed_domains = ['gdgpo.czt.gd.gov.cn']
    # start_urls = ['http://gdgpo.czt.gd.gov.cn/']
    
    def start_requests(self):
        header = {
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

        data = '{"pageNumber":"1","pageSize":"10","sortType":"0","sortOrder":"asc","goodsClassGuid":"ff80808174c46e510174c49e58c60033","addressid":""}'


        return [
            scrapy.Request(
                "https://gdgpo.czt.gd.gov.cn/gateway/gp-provide/api/v2/searchProvideSortInformation",
                method = "POST",
                callback= self.parse,
                body = data,
                headers=header
            )
        ]

    def parse(self, response):
        print(response.body.decode("utf-8"))
