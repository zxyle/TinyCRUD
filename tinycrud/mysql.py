#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: MySQL

import re
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
                                          charset=self.u.params.get('charset', 'utf8mb4'),
                                          cursorclass=pymysql.cursors.DictCursor)
        self._open = False
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
        self.execute(sql, values)

    def insert_many(self, tb, doc_list):
        """

        :param tb: mysql table name
        :param doc_list: [{}, {}, ...]
        :return:
        """
        for doc in doc_list:
            self.insert(tb, doc)

    def _get_cursor(self):
        if not self._open and not self.cursor:
            self.cursor = self.connection.cursor()
            self._open = True
        return self.cursor

    def execute(self, sql, data=None):
        """

        :param sql: SQL statement
        :param data:
        :return:
        """
        cursor = self._get_cursor()
        cursor.execute(sql, data)

        # TODO fetchall fetchone fetchmany
        rows = cursor.fetchall()
        if len(rows) == 1:
            return rows[0]
        elif len(rows) > 1:
            return rows

    def create_db(self, db_name=""):
        if not db_name:
            raise ValueError("db name not allowed to be empty.")

        sql = f"CREATE DATABASE IF NOT EXISTS `{db_name}` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
        self.execute(sql)
        print("create database: `{}` success.".format(db_name))

    def drop_db(self, db_name=""):
        sql = f"DROP DATABASE IF EXISTS {db_name};"
        self.execute(sql)
        print("drop database: `{}` success.".format(db_name))

    def create_tb(self, tb=""):
        sql = f"""
        CREATE TABLE IF NOT EXISTS `{tb}`(
           id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
           create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
           modify_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
           name VARCHAR(20) NULL,
           age TINYINT UNSIGNED NULL,
           address VARCHAR(50) NULL
        )ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;"""
        self.execute(sql)
        print("create table: `{}` success.".format(tb))

    def drop_tb(self, tb=""):
        sql = f"DROP TABLE IF EXISTS {tb};"
        self.execute(sql)
        print("drop table: `{}` success.".format(tb))

    def query(self, tb, condition):
        condition_sql = self._where(condition)

        sql = f"SELECT * FROM {tb} {condition_sql};"
        results = self.execute(sql)
        return results

    def update(self, tb, doc, condition):
        # build sql
        fields, values = [], []
        for field, value in doc.items():
            fields.append(f"`{field}`=%s")
            values.append(value)

        fields_sql = ", ".join(fields)

        condition_sql = self._where(condition)
        sql = f"UPDATE `{tb}` SET {fields_sql} {condition_sql};"
        self.execute(sql, values)
        print("update success.")

    def delete(self, tb, condition):
        condition_sql = self._where(condition)
        sql = f"DELETE FROM {tb} {condition_sql};"
        self.execute(sql)

    def _where(self, condition):
        condition_list = []
        for k, v in condition.items():
            operator, v = self._parse(v)
            if isinstance(v, str):
                condition_list.append(f'{k}{operator}"{v}"')
            else:
                condition_list.append(f'{k}{operator}{v}')

        condition_sql = " AND ".join(condition_list)
        return f"WHERE {condition_sql}"

    @staticmethod
    def _parse(v):
        pattern = re.findall(r"[>=<!]=?", v)
        if not pattern:
            return "=", v
        else:
            value = v.replace(pattern[0], "")
            if value.isnumeric():
                value = int(value)
            return pattern[0], value

    def _commit(self):
        try:
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()
        else:
            pass

    def __del__(self):
        """close connection and cursor"""
        self._commit()
        self._get_cursor().close()
        self.connection.close()

    def __repr__(self):
        key = "version()"
        sql = f"SELECT {key};"
        version = self.execute(sql).get(key)
        return "MySQL:<{}> at {}.".format(version, self.connection.host_info)
