#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/25
# Desc: 

from urllib.parse import urlparse, quote, unquote


def build_url(url, params):
    """
    :argument:
    - `url`:  string, received base_url like this: https://www.example.com
    - `params`:  dict, received params like this: {'name': 'zx', 'age': 11}

    :return string https://www.example.com/?name=zx&age=11
    """
    if not isinstance(url, str):
        raise TypeError

    if not isinstance(params, dict):
        raise TypeError

    if url[-1] != '?':
        url += '?'

    key_values = []
    for k, v in params.items():
        if not v:
            continue
        value = quote(str(v))
        key_values.append(f"{k}={value}")

    return url + "&".join(key_values)


def unpack_url(url):
    """
    :argument:
    - `url`:  string, received base_url like this:
             https://www.example.com/?name=zx&age=11
    :return ('https://www.example.com', {'name': 'zx', 'age': 11})
    :rtype tuple
    """
    if not isinstance(url, str):
        raise TypeError

    part = url.split('?')
    if len(part) < 2:
        raise ValueError

    base_url = url.split('?')[0]
    params_url = url.split('?')[1]

    params = params_url.split('&')
    values = dict()
    for param in params:
        key, value = param.split('=')
        if value.isnumeric():
            value = int(value)
        else:
            value = unquote(value)
        values.update({key: value})

    return base_url, values


class UriParser:
    def __init__(self, uri):
        self.uri = uri
        self.handle = urlparse(self.uri)

    @property
    def scheme(self):
        return self.handle.scheme

    @property
    def host(self):
        return self.handle.hostname

    @property
    def port(self):
        return self.handle.port

    @property
    def user(self):
        return self.handle.username

    @property
    def password(self):
        return self.handle.password

    @property
    def db(self):
        path = self.handle.path
        return path.replace("/", "")

    @property
    def params(self):
        _, param = unpack_url(self.uri)
        return param

    def __repr__(self):
        return "URI:"
