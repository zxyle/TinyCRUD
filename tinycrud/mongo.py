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


class Mongo(DataBase):
    def __init__(self, uri=None, db=None):
        self.uri = uri or DEFAULT_MONGODB_URI
        self.tz = pytz.timezone('Asia/Shanghai')

        client = pymongo.MongoClient(self.uri)
        self.db = client[db]

    def insert(self, doc, col="test"):
        post = self.db[col]
        try:
            post.insert_one(doc)
        except DuplicateKeyError:
            print("重复丢弃")
        else:
            print("write success.")

    def query(self, tb_name, condition):
        pass

    def ensure_index(self):
        pass

    def __repr__(self):
        return "Mongo:{}".format(self.db.version)
