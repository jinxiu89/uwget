#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/4.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.modules.PermissionGroup import PermissionGroup as Model
from utils.admin.common import packing_error


@admin.route('/permission/role', methods=['GET', 'POST'])
def admin_permission_role():
    return render_template('admin/permission/role.html')


@admin.route('/permission/role/add', methods=['GET', 'POST'])
def admin_permission_role_add():
    return render_template('admin/permission/add_role.html')
