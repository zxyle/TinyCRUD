#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019/7/26
# Desc: 

import os

from tinycrud.mysql import MySQL

ENV = os.getenv("ENV")
if ENV == "CI":
    uri = "mysql+pymysql://root@localhost:3306/test?charset=utf8mb4"
else:
    uri = "mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4"
my = MySQL(uri)


def test_insert():
    table_name = "students"
    my.drop_tb(table_name)
    my.create_tb(table_name)
    insert_data = {"name": "zx", "age": 1, "address": "Hangzhou"}
    my.insert(table_name, insert_data)
    rows = my.query(table_name, {})
    assert rows.get("name") == insert_data.get("name") and rows.get("address") == insert_data.get("address")
