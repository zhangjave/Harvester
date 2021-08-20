#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Author : ZhangJW
# License: MIT License
# File   : application.py
# Date   : 2021/8/20 13:42
# Version: 0.0.1
# Description:



class Setting(object):
    def __init__(self):
        pass


class CloudDataExportor(object):
    def __init__(self):
        pass


class Application(object):
    def __init__(self, name):
        self.name = name

    # def submit_account(self):
    #     pass
    #
    # def remove_account(self):
    #     pass


class Account(object):
    def __init__(self, account):
        self.login_account = account
        self.fetch_complete = False

    @property
    def is_phone_number(self):
        pass

    @property
    def is_email(self):
        pass

    @property
    def is_all_numbers(self):
        pass


class BaseSubject(object):
    name =''

    def __init__(self, *args,  **kwargs):
        pass


class Request(object):
    def __init__(self):
        pass


class Response(object):
    def __init__(self):
        pass





