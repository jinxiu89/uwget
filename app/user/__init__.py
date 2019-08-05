#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')
from .auth import *
from .user import *
