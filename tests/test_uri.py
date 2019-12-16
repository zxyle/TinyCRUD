#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 


from crudlib.config import DEFAULT_MONGODB_URI, DEFAULT_MYSQL_URI
from crudlib.uri import UriParser


LOCALHOST = ("localhost", "127.0.0.1", "LOCALHOST")


def test_mysql_uri():
    u = UriParser(DEFAULT_MYSQL_URI)
    assert u.host in LOCALHOST
    assert u.port == 3306
    assert u.password == "123456"
    assert u.db == "test"
    assert u.user == "root"
    assert u.scheme == "mysql+pymysql"
    assert u.params == {'charset': 'utf8mb4'}


def test_mongodb_uri():
    u = UriParser(DEFAULT_MONGODB_URI)
    assert u.host in LOCALHOST
    assert u.password is None
    assert u.db == "test"
    assert u.user is None
    assert u.scheme == "mongodb"
