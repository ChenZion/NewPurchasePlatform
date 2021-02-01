# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShengcaidataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provideGuid = scrapy.Field()
    """详情ID"""
    goodsClassGuid = scrapy.Field()
    """定点服务类型ID"""
    goodsClassName = scrapy.Field()
    """定点服务类型名称"""
    supplierGuid = scrapy.Field()
    """供应商唯一标识ID"""
    linkMan = scrapy.Field()
    """联系人姓名"""
    mobile = scrapy.Field()
    """联系人电话"""
    city = scrapy.Field()
    """城市"""
    address = scrapy.Field()
    """地址"""
    provideName = scrapy.Field()
    """公司名称"""
    picturePath = scrapy.Field()
    """LOGO图片"""
    total = scrapy.Field()
    """成交数量"""

