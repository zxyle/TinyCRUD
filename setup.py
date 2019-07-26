from setuptools import setup

requires = [
    "pymongo==3.8.0",
    "pymysql==0.9.3",
    "pytz==2019.1",
    "redis==3.2.1",
]

tests_require = [
    "pytest==5.0.1",
]


# python setup.py sdist upload
setup(
    name="TinyCRUD",
    version="0.1.1",
    author="Zheng",
    author_email="zxyful@gmail.com",
    description="tinycrud",
    long_description="",
    license="MIT",
    url="https://github.com/zxyle/TinyCRUD",
    packages=['tinycrud'],
    install_requires=requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
