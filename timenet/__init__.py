# coding=utf-8
from __future__ import unicode_literals, absolute_import
from .client import TimenetClient

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("timenet").version
except pkg_resources.DistributionNotFound:
    __version__ = "0.1.0"
