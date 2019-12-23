#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/24.
from app.admin import admin
from flask import render_template, request, jsonify, session
from forms.language.form import Form
from app.modules.Language import Language
from utils.admin.common import packing_error
from app.admin.decorate import is_login


@admin.route('/language', methods=['GET', 'POST'])
@is_login
def admin_language_list():
    if request.method == "GET":
        data, count = Language.all()
        return render_template('admin/language/index.html', data=data, count=count)


@admin.route('/language/add', methods=['GET', 'POST'])
@is_login
def admin_language_add():
    form = Form()
    if request.method == "GET":
        return render_template('admin/language/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/language/edit/<int:id>', methods=['GET', 'POST'])
@is_login
def admin_language_edit(id):
    form = Form()
    data = Language.by_id(id)
    if request.method == "GET":
        form.name.data = data.name
        form.code.data = data.code
        form.status.data = data.status
        return render_template('admin/language/edit.html', form=form, data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.update(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/language/stop/<int:id>', methods=['GET', 'POST'])
@is_login
def admin_language_stop(id):
    if request.method == "GET":
        data = Language.by_id(id)
        data.status = 2
        result = Language.change_status(data)
        return jsonify(result)


@admin.route('/language/start/<int:id>', methods=['GET', 'POST'])
@is_login
def admin_language_start(id):
    if request.method == "GET":
        data = Language.by_id(id)
        data.status = 1
        result = Language.change_status(data)
        return jsonify(result)
