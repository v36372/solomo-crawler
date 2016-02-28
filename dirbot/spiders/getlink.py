# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import json
import base64
from dirbot.items import Website
from urlparse import urljoin

class GetlinkSpider(Spider):
    name = "getlink"
    allowed_domains = ["hotdeal.vn"]
    start_urls = [
        'http://www.hotdeal.vn/ho-chi-minh/deal-hot/?page=1'
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[contains(@class, "product product-kind")]')
        with open('listlink.txt', 'w') as outfile:
            for site in sites:
                url = ""
                if site.xpath('div[@class="product__image"]/div[@class="item__location"]').extract() != []:
                    url +=  "http://www.hotdeal.vn" + site.xpath('div[@class="product__header"]/h3/a/@href').extract()[0]
                    url += "\n"
                    outfile.write(url)
        with open("listdeal.csv","w") as listdealfile:
            listdealfile.write("name,description,link,newprice,discount,oldprice,img,location")
            listdealfile.write('\n')
