from setuptools import setup

requires = [
    "pymongo==3.8.0",
    "pymysql==0.9.3",
    "pytz==2019.1",
    "redis==3.2.1",
]
# python setup.py sdist upload
setup(
    name="TinyCRUD",
    version="0.0.2",
    author="Zheng",
    author_email="zxyful@gmail.com",
    description="tinycrud",
    long_description="",
    license="MIT",
    url="https://github.com/zxyle/TinyCRUD",
    packages=['tinycrud'],
    install_requires=requires,
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
