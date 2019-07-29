#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/26
# Desc: 


from tinycrud.config import DEFAULT_REDIS_URI
from tinycrud.redisHandle import Redis

r = Redis(DEFAULT_REDIS_URI)


def test_insert():
    insert_data = {"name": "Hangzhou"}
    r.insert("cities", insert_data)

    result = r.query("cities", {})
    print(result)
    assert result == insert_data
