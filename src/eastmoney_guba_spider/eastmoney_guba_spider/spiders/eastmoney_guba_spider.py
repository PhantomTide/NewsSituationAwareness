"""
eastmoney_guba_spider 东方财富股吧爬虫
"""

import scrapy

class EastMoneyGubaSpider(scrapy.Spider):
    """
    EastMoneyGubaSpider class
    """
    name = "eastmoney_guba"
    allowed_domains = ["eastmoney.com"]
    start_urls = []