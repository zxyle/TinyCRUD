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
        self.u = UriParser(self.uri)

        pool = redis.ConnectionPool(host=self.u.host, port=self.u.port, db=self.u.db,
                                    password=self.u.password)
        self.r = redis.Redis(connection_pool=pool)

    def test(self):
        return self.r.ping()

    def insert(self, tb, doc):
        self.r.set(tb, str(doc))

    def query(self, tb, condition):
        result = self.r.get(tb)
        if isinstance(result, bytes):
            return eval(str(result, encoding="utf-8"))

        return result

    def update(self, tb, doc, condition):
        pass

    def __repr__(self):
        version = self.r.info("Server").get("redis_version")
        return "Redis: {}".format(version)
