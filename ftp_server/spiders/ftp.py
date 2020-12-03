# -*- coding: utf-8 -*-
import scrapy


class FtpSpider(scrapy.Spider):
    name = 'ftp'
    allowed_domains = ['sites.google.com']
    start_urls = ['https://sites.google.com/view/bdixftpserverlist/media-ftp-servers']

    def parse(self, response):
        ftps = response.xpath('//*[@class="NsaAfc"]')
        for ftp in ftps:
            yield {
                'FTP': ftp.xpath('.//p/text()').get()
            }
