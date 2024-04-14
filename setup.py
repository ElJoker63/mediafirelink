# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name="mediafirelink",
    version="1.0.0",
    packages=["mediafirelink"],
    url="https://github.com/ElJoker63/mediafirelink/",
    license="MIT",
    author="Victor Morejon Garriga",
    author_email="eljoker630@gmail.com",
    description="Python module Mediafire ",
    long_description=open("README.md", "r").read(),  # pylint: disable=R1732
    long_description_content_type="text/markdown",
    install_requires=("requests",),
)