#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/1.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.modules.Permission import Permission
from app.modules.PermissionGroup import PermissionGroup
from utils.admin.common import packing_error
from forms.permission.Permission import PermissionForm
from app.admin.decorate import require_login


@admin.route('/permission', methods=['GET'])
@require_login
def admin_permission():
    data, count = Permission.all()
    return render_template('admin/permission/permission.html', data=data, count=count)


@admin.route('/permission/group/<int:group_id>', methods=['GET', 'POST'])
@require_login
def admin_permission_list(group_id):
    data, count = Permission.by_groupId(group_id)
    return render_template('admin/permission/permission.html', data=data, count=count, group_id=group_id)


@admin.route('/permission/<int:group_id>/add', methods=['GET', 'POST'])
@require_login
def admin_permission_add(group_id=None):
    form = PermissionForm()
    form.group_id.choices = PermissionGroup.choices()
    if request.method == 'GET':
        if group_id is not None:
            form.group_id.data = group_id
        return render_template('admin/permission/add_permission.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/permission/edit/<int:id>', methods=['GET', 'POST'])
@require_login
def admin_permission_edit(id):
    form = PermissionForm()
    form.group_id.choices = PermissionGroup.choices()
    data = Permission.by_id(id)
    if request.method == "GET":
        form.group_id.data = data.group_id
        form.name.data = data.name
        form.code.data = data.code
        return render_template('admin/permission/edit_permission.html', form=form, data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.update(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})
