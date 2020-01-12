#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/26
# Desc: 

from crudlib.databases import MySQL

uri = "mysql+pymysql://root:123456@localhost:33060/test?charset=utf8mb4"
my = MySQL(uri, debug=True)
test_table = "developers"
test_data = {"name": "zxyle", "age": 25, "address": "Hangzhou"}


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


def test_rollback():
    my.insert(test_table, test_data)
    my.rollback()
    assert my.query(test_table) is None
