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
test_table = "student"
test_data = {"name": "zx", "age": 1, "address": "Hangzhou"}


def test_insert():
    my.drop_tb(test_table)
    my.create_tb(test_table)
    assert my.insert(test_table, test_data) is not None


def test_query():
    rows = my.query(test_table)
    rows.pop("id")
    rows.pop("create_time")
    rows.pop("modify_time")
    assert rows == test_data


def test_update():
    update_data = {"age": 20}
    condition = {}
    my.update(test_table, update_data, condition)
    my.commit()

    rows = my.query(test_table)
    assert rows.get("age") == update_data.get("age")


def test_delete():
    condition = {}
    my.delete(test_table, condition)

    rows = my.query(test_table)
    assert rows is None


def test_insert_many():
    pass
