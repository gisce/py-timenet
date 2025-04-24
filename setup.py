# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="timenet",
    version="0.1.0",
    description="Client Python per interactuar amb l'API de Timenet",
    author="GISCE-TI",
    author_email="devel@gisce.net",
    url="https://github.com/gisce/py-timenet",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
)

