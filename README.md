# TinyCRUD
*One API, More Database.*

[![Build Status](https://travis-ci.org/zxyle/TinyCRUD.svg?branch=master)](https://travis-ci.org/zxyle/TinyCRUD)

Implement a set of interfaces to operate databases such as MySQL, MongoDB, and Redis.
His goal is not to build a powerful ORM framework like [SQLAlchemy](https://github.com/zzzeek/sqlalchemy),
just to satisfy the most basic CRUD operations.

## Quick Start
```python
from tinycrud.mysql import MySQL

my = MySQL()
my.insert("cities", {"name":"Shanghai"})
```

## Installation
```
pip install tinycrud
```

## Features
* MySQL
* MongoDB
* Redis


## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for more details.
