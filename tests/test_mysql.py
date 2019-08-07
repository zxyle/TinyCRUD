#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/26
# Desc: 

import os

from tinycrud.config import DEFAULT_MYSQL_URI
from tinycrud.databases import MySQL

ENV = os.getenv("ENV")
if ENV == "CI":
    # No password by default in Travis CI ENV
    uri = "mysql+pymysql://root@localhost:3306/test?charset=utf8mb4"
else:
    uri = DEFAULT_MYSQL_URI
my = MySQL(uri, debug=True)
table_name = "student"
insert_data = {"name": "zx", "age": 1, "address": "Hangzhou"}


def test_insert():
    my.drop_tb(table_name)
    my.create_tb(table_name)
    assert my.insert(table_name, insert_data) is not None


def test_query():
    rows = my.query(table_name)
    assert rows.get("name") == insert_data.get("name") and rows.get("address") == insert_data.get("address")


def test_update():
    update_data = {"age": 20}
    condition = {}
    my.update(table_name, update_data, condition)
    my.commit()

    rows = my.query(table_name)
    assert rows.get("age") == update_data.get("age")


def test_delete():
    condition = {}
    my.delete(table_name, condition)

    rows = my.query(table_name)
    assert rows is None
