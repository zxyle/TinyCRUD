# TinyCRUD
*One API, More Database.*

[![Build Status](https://travis-ci.org/zxyle/TinyCRUD.svg?branch=master)](https://travis-ci.org/zxyle/TinyCRUD)
[![pypi version](https://img.shields.io/pypi/v/tinycrud.svg)](https://pypi.org/project/TinyCRUD/)
[![GitHub license](https://img.shields.io/github/license/zxyle/TinyCRUD.svg)](https://github.com/zxyle/TinyCRUD/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/tinycrud/badge/?version=latest)](https://tinycrud.readthedocs.io/en/latest/?badge=latest)

Implement a set of interfaces to operate databases such as MySQL, MongoDB, and Redis.
His goal is not to build a powerful ORM framework like [SQLAlchemy](https://github.com/zzzeek/sqlalchemy),
just to satisfy the most basic CRUD operations.

## Quick Start
```python
from tinycrud.databases import MySQL, Mongo, Redis

my = MySQL()
my.insert(tb="student", doc={"name": "zx"})

rows = my.query(tb="student", condition={"age": ">=18"})

# Use SQL directly
my.execute("SELECT User FROM mysql.user;")
```

## Installation
```bash
pip install tinycrud
```

## Features
* MySQL
* MongoDB
* Redis


## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for more details.

## Sponsors
* [JetBrains](https://www.jetbrains.com/) - Offer free JetBrains Open Source license.
