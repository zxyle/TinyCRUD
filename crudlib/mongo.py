#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

import pymongo
import pytz
from pymongo.errors import DuplicateKeyError

from crudlib.base import DataBase
from crudlib.config import DEFAULT_MONGODB_URI
from crudlib.uri import UriParser


class Mongo(DataBase):
    def __init__(self, uri=None):
        self.uri = uri or DEFAULT_MONGODB_URI
        self.tz = pytz.timezone('Asia/Shanghai')
        u = UriParser(self.uri)
        client = pymongo.MongoClient(self.uri)
        self.db = client[u.db]

    def insert(self, tb, doc):
        post = self.db[tb]
        try:
            post.insert_one(doc)
        except DuplicateKeyError:
            print("duplicate.")
        else:
            print("write success.")

    def query(self, tb, condition=None):
        post = self.db[tb]
        return [row for row in post.find(condition)]

    def update(self, tb, doc, condition):
        pass

    def ensure_index(self):
        pass

    def __repr__(self):
        return "Mongo:{}".format(self.db.version)
