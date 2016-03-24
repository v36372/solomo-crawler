# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import json
import base64
from dirbot.items import Website
from urlparse import urljoin


class HotdealSpider(Spider):
    name = "hotdeal"
    allowed_domains = ["hotdeal.vn"]

    f = open("listlink.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        sel = Selector(response)
        # sites = sel.xpath('//div[@class="product__details"]')

        with open('listdeal.csv', 'a') as outfile:
            # for site in sites:
            outfile.write('"')
            outfile.write(sel.xpath('//div[@class="product__header"]/h1/text()').extract()[0].encode('utf-8'))
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//div[@class="product__description"]/p/text()').extract()[0].encode('utf-8'))
            outfile.write('"')
            outfile.write(',')

            outfile.write(response.request.url)
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//span[@itemprop="price"]/text()').extract()[0].strip())
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//span[@class="price__discount"]/text()').extract()[0].strip())
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//span[@class="price price--list-price"]/span[@class="price__value"]/text()').extract()[0].strip())
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//div[@class="gallery__image media-gallery"]/a/img/@src').extract()[0].strip())
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(sel.xpath('//ul[@class="feature-list"]/li/div/text()').extract()[0].encode('utf-8').strip())
            outfile.write('"')
            outfile.write(',')

            link = sel.xpath('//a[@class="media-link"]/img/@src').extract()[0].encode('utf-8').strip()
            outfile.write('"')
            outfile.write(link[link.find("label:H",0)+8:link.find(",",link.find("label:H",0))])
            outfile.write('"')
            outfile.write(',')

            outfile.write('"')
            outfile.write(link[link.find(",",link.find("label:H",0))+1:link.find("&",link.find(",",link.find("label:H",0)))])
            outfile.write('"')
            outfile.write(',')

            outfile.write('\n')
