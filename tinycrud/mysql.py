#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

import pymysql

from tinycrud.base import DataBase
from tinycrud.config import DEFAULT_MYSQL_URI
from tinycrud.uri import UriParser


class MySQL(DataBase):
    def __init__(self, uri=None):
        self.uri = uri or DEFAULT_MYSQL_URI
        self.u = UriParser(self.uri)
        self.connection = pymysql.connect(host=self.u.host,
                                          port=self.u.port,
                                          user=self.u.user,
                                          password=self.u.password,
                                          db=self.u.db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.open = False
        self.cursor = None

    def insert(self, tb, doc):
        """

        :param tb: mysql table name
        :param doc: {"name": "tinycrud"}
        :return:
        """
        # build sql
        fields, values = [], []
        for field, value in doc.items():
            fields.append(f"`{field}`")
            values.append(value)

        fields_sql = ", ".join(fields)
        values_sql = ", ".join(["%s" for _ in range(len(values))])
        sql = f"INSERT INTO `{tb}` ({fields_sql}) VALUES ({values_sql});"
        self._execute(sql, values)

    def insert_many(self, tb, doc_list):
        for doc in doc_list:
            self.insert(tb, doc)

    def _get_cursor(self):
        if not self.open:
            self.cursor = self.connection.cursor()
            self.open = True
        return self.cursor

    def _execute(self, sql, data=None):
        cursor = self._get_cursor()
        cursor.execute(sql, data)

        # TODO fetchall fetchone fetchmany
        rows = cursor.fetchall()
        if len(rows) == 1:
            return rows[0]
        elif len(rows) > 1:
            return rows

        try:
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()
        else:
            print("execute success.")

    def create_db(self, db_name=""):
        if not db_name:
            raise ValueError("db name not allowed to be empty.")

        sql = f"CREATE DATABASE `{db_name}` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
        self._execute(sql)

    def drop_db(self, db_name=""):
        sql = f"DROP DATABASE IF EXISTS {db_name};"
        self._execute(sql)

    def create_tb(self, table_name=""):
        sql = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}`(
           id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
           name VARCHAR(20) NULL,
           age TINYINT UNSIGNED NULL,
           address VARCHAR(50) NULL
        )ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"""
        self._execute(sql)

    def drop_tb(self, tb=""):
        sql = f"DROP TABLE IF EXISTS {tb};"
        self._execute(sql)

    def query(self, tb, condition):
        # TODO 复杂的话 直接提供sql操作
        condition_sql = " AND ".join([f"{k}=\"{v}\"" for k, v in condition.items()])
        if condition_sql:
            condition_sql = f"WHERE {condition_sql}"
        sql = f"SELECT * FROM {tb} {condition_sql};"
        results = self._execute(sql)
        return results

    def __del__(self):
        """close connection and cursor"""
        self._get_cursor().close()
        self.connection.close()

    def __repr__(self):
        sql = "SELECT version() FROM dual;"
        version = self._execute(sql).get("version()")
        return "MySQL:<{}> at {}.".format(version, self.connection.host_info)
