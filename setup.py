#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# name:      setup.py

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "TTS",
    version = "0.0.1",
    python_requires=">=3.0",
    description = "Mozilla TTS",
    license = "Mozilla Public License Version 2.0",
    keywords = "Mozilla TTS",
    url = "",
    packages= find_packages(),
    install_requires=required,
    scripts=[
        "txt2wav.py"
    ],
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License Version 2.0",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
