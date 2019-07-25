#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

from urllib.parse import urlparse


class UriParser:
    def __init__(self, uri):
        self.uri = uri
        self.handle = urlparse(self.uri)

    @property
    def scheme(self):
        return self.handle.scheme

    @property
    def host(self):
        return self.handle.hostname

    @property
    def port(self):
        return self.handle.port

    @property
    def user(self):
        return self.handle.username

    @property
    def password(self):
        return self.handle.password

    @property
    def db(self):
        path = self.handle.path
        return path.replace("/", "")

    def __repr__(self):
        return "URI:"
