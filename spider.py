#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : ZhangJW
# License: MIT License
# File   : spider.py
# Date   : 2021/8/20 14:09
# Version: 0.0.1
# Description:


class BaseSpider(object):
    name = ''
    start_urls = []

    def __init__(self, *args, **kwargs):
        self.crawler = kwargs.get('crawler', None)
        # self.logger = logging.getLogger(__name__)

    def spider_started(self):
        pass

    def spider_idle(self):
        pass

    def spider_stopped(self):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, callback=self.parse)

    def parse(self, response):
        raise NotImplementedError

    def process_request(self, request):
        pass

    def process_response(self, response):
        pass

    def process_item(self, item):
        raise NotImplementedError

    def __repr__(self):
        return '<{} name="{}">'.format(self.__class__.__name__, self.name)
