# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wechat-web-auth",
    version="0.1.0",
    keywords=("wechat", "web auth"),
    description=u"微信公众平台网页授权获取用户信息python封装",
    long_description=open("README.md").read(),
    license="MIT License",

    url="https://github.com/jinuljt/wechat-web-auth",
    author="Juntao Liu",
    author_email="jinuljt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=map(lambda x: x.replace('==', '>='), open("requirements.txt").readlines()),
    )
