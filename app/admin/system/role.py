#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/4.
from app.admin import admin
from flask import render_template, request, jsonify, session, url_for
from app.modules.Roles import Roles
from app.modules.PermissionGroup import PermissionGroup as Group
from utils.admin.common import packing_error
from forms.permission.Role import RoleForm
from app.admin.decorate import is_login


@admin.route('/permission/role', methods=['GET', 'POST'])
@is_login
def admin_permission_role():
    if request.method == 'GET':
        data, count = Roles.all()
        return render_template('admin/permission/role.html', data=data, count=count)


@admin.route('/permission/role/add', methods=['GET', 'POST'])
@is_login
def admin_permission_role_add():
    form = RoleForm()
    if request.method == 'GET':
        return render_template('admin/permission/add_role.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/permission/role/edit/<int:id>', methods=['GET', 'POST'])
@is_login
def admin_permission_role_edit(id):
    form = RoleForm()
    data = Roles.by_id(id)
    if request.method == "GET":
        form.name.data = data.name
        return render_template('admin/permission/edit_role.html', form=form, data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.update(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/permission/role/setting/<int:id>', methods=['GET', 'POST'])
@is_login
def admin_set_permission(id):
    group = Group.with_permission()
    return render_template('admin/permission/set_permission.html', group=group)
