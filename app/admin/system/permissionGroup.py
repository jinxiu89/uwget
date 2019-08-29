#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/28.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.modules.PermissionGroup import PermissionGroup as Model
from utils.admin.common import packing_error
from forms.permission.PermissionGroup import PermissionGroup


@admin.route('/permission/group/', methods=['GET'])
def admin_permission_group():
    data, count = Model.all()
    if request.method == "GET":
        return render_template('admin/permission/group.html', data=data, count=count)


@admin.route('/permission/group/add', methods=['GET', 'POST'])
def admin_permissionGroup_add():
    form = PermissionGroup()
    if request.method == "GET":
        return render_template('/admin/permission/add_group.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/permission/group/edit/<int:id>', methods=['GET', 'POST'])
def admin_permissionGroup_edit(id):
    form = PermissionGroup()
    data = Model.by_id(id)
    if request.method == 'GET':
        form.name.data = data.name
        return render_template('admin/permission/edit_group.html', form=form, data=data)
    if request.method == 'POST':
        if form.validate_on_submit():
            result = form.update(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})
