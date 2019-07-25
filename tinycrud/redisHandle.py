#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

import redis

from tinycrud.base import DataBase
from tinycrud.config import DEFAULT_REDIS_URI
from tinycrud.uri import UriParser


class Redis(DataBase):
    def __init__(self, uri=None):
        self.uri = uri or DEFAULT_REDIS_URI
        self.handle = UriParser(self.uri)

        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0,
                                    password=None)
        self.r = redis.Redis(connection_pool=pool)

    def test(self):
        return self.r.ping()

    def query(self, tb_name, condition):
        pass

    def __repr__(self):
        version = self.r.info("Server").get("redis_version")
        return "Redis: {}".format(version)
