#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

import pymongo
import pytz
from pymongo.errors import DuplicateKeyError

from tinycrud.base import DataBase
from tinycrud.config import DEFAULT_MONGODB_URI
from tinycrud.uri import UriParser


class Mongo(DataBase):
    def __init__(self, uri=None):
        self.uri = uri or DEFAULT_MONGODB_URI
        self.tz = pytz.timezone('Asia/Shanghai')
        self.u = UriParser(self.uri)
        client = pymongo.MongoClient(self.uri)
        self.db = client[self.u.db]

    def insert(self, tb_name, doc):
        post = self.db[tb_name]
        try:
            post.insert_one(doc)
        except DuplicateKeyError:
            print("duplicate.")
        else:
            print("write success.")

    def query(self, tb_name, condition):
        post = self.db[tb_name]
        return [row for row in post.find(condition)]

    def ensure_index(self):
        pass

    def __repr__(self):
        return "Mongo:{}".format(self.db.version)
