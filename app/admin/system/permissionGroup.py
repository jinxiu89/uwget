#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/28.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.modules import PermissionGroup
from utils.admin.common import packing_error


@admin.route('/permission/group/', methods=['GET'])
def admin_permission_group():
    if request.method == "GET":
        return render_template('admin/permission/group.html')
