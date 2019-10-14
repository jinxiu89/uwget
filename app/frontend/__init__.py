#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask import Blueprint

frontend = Blueprint('frontend', __name__, url_prefix='/')
from .context import *
from .filter import *
from .decorate import *
from .home.index import *
from .post import *
