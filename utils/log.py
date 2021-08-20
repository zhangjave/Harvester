#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : ZhangJW
# License: MIT License
# File   : log.py
# Date   : 2021/8/20 14:44
# Version: 0.0.1
# Description:


# import logging

import logging.handlers
import os
from logging.handlers import RotatingFileHandler
import time
import sys
import pathlib


def get_logger(name="Harvester", fold_id=None):
    logger_param = {
        'appname': name,
        'computername': os.environ['COMPUTERNAME'],
    }
    if fold_id is None:
        log_folder = '%s/Log/' % (pathlib.Path(sys.argv[0]).parent.parent.__str__())
    else:
        log_folder = '%s/Log/%s/' % (pathlib.Path(sys.argv[0]).parent.parent.__str__(), fold_id)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_name = log_folder + name + '.log'
    return Logger(log_name, **logger_param)


class Logger(logging.Logger):
    def __init__(self, filename=None, **kwargs):
        super(Logger, self).__init__(self)
        # 日志文件名
        if filename is None:
            filename = 'log.log'
        self.filename = filename

        # 用于写入日志文件
        fh = MyRotatingFileHandler(self.filename, maxBytes=20*1024*1024)
        fh.setLevel(logging.DEBUG)

        # 用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [{}] [%(process)s] [%(thread)s] [%(filename)s:%(lineno)d] [{}] %(message)s'.format(
                kwargs.get('computername', ''), kwargs.get('appname', '')
            )
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)


class MyRotatingFileHandler(RotatingFileHandler):

    def doRollover(self):
        '''重写doRollover函数'''
        if self.stream:
            self.stream.close()
            self.stream = None
        dfn = self.rotation_filename(self.new_filename())
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()

    def new_filename(self):
        pos = self.baseFilename.rfind('.')
        time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        if pos != -1:
            filename = self.baseFilename[:pos]
            ext = self.baseFilename[pos+1:]
            return '{}_{}.{}'.format(filename, time_str, ext)
        return '{}_{}'.format(self.baseFilename, time_str)


