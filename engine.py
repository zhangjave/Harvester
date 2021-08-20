#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : ZhangJW
# License: MIT License
# File   : engine.py
# Date   : 2021/8/17 14:18
# Version: 0.0.1
# Description:
import threading
from queue import Queue, Empty
from random import randint

import requests
import time

__version__ = '0.0.2'
__author__ = 'Chris'


__all__ = ['CrawlerEngine']



class CrawlerProcess(object):
    def __init__(self, settings=None):
        pass


class CrawlerEngine(object):
    def __init__(self, concurrent_requests=128, download_delay=0, download_timeout=5, retry_on_timeout=False, queue_size=1024):
        """

        :param concurrent_requests:
        :param download_delay:
        :param download_timeout:
        :param retry_on_timeout:
        :param queue_size:
        """
        self.status = False
        self.concurrent_requests = concurrent_requests
        self.download_delay = download_delay
        self.engine_idle_timeout = 1.5 * download_timeout
        self.download_timeout = download_timeout
        self.retry_on_download_timeout = retry_on_timeout
        self._requests_queue = Queue(queue_size)
        self._spiders = {}
        self._seen = set()

    def start(self):
        """
        开启引擎
        :return:
        """
        pass

    def shutdown(self):
        """
        关闭
        :return: None
        """
        self.status = False

    def submit(self):
        pass



