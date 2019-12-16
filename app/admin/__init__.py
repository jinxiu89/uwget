#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
import os
from flask import Blueprint, current_app, url_for, request
from utils.admin.upload import upload_image, change_filename, jsonify

admin = Blueprint('admin', __name__, url_prefix='/admin')
from .index.dashboard import *
from .content.category import *
from .content.posts import *
from .system import (language, permissionGroup, permission, role, user)
from .context import *
from .filter import *
from .decorate import *
