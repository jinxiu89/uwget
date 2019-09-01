#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/1.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.modules.PermissionGroup import PermissionGroup
from utils.admin.common import packing_error
from forms.permission.Permission import PermissionForm


@admin.route('/permission', methods=['GET'])
def admin_permission():
    return render_template('admin/permission/permission.html')


@admin.route('/permission/add', methods=['GET', 'POST'])
def admin_permission_add():
    form = PermissionForm()
    form.group_id.choices = PermissionGroup.choices()
    if request.method == 'GET':
        return render_template('admin/permission/add_permission.html', form=form)


