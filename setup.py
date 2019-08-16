# https://pypi.org/project/TinyCRUD/

from setuptools import setup, find_packages

requires = [
    "pymongo==3.8.0",
    "pymysql==0.9.3",
    "pytz==2019.1",
    "redis==3.2.1",
]

tests_require = [
    "pytest==5.0.1",
]

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

# distribution:
# python setup.py sdist bdist_wheel
# twine upload dist/*

setup(
    name="TinyCRUD",
    version="0.1.8",
    author="Zheng",
    author_email="zxyful@gmail.com",
    description="One API, More Database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/zxyle/TinyCRUD",
    packages=find_packages(),
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
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        # "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
