#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from app.admin import admin
from flask import render_template, request, jsonify
from app.forms.category.form import Form
from app.modules.Category import Category
from app.utils.admin.common import packing_error
from app.admin.decorate import require_login


@admin.route('/category', methods=['GET'])
@require_login
def admin_category_list():
    if request.method == 'GET':
        data, count = Category.all()
        return render_template('admin/category/index.html', data=data, count=count)


@admin.route('/category/add', methods=['GET', 'POST'])
@require_login
def admin_category_add():
    form = Form()
    form.pid.choices = Category.choices()
    if request.method == "GET":
        return render_template('admin/category/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/category/edit/<int:id>', methods=['GET', 'POST'])
@require_login
def admin_category_edit(id):
    form = Form()
    form.pid.choices = Category.choices()
    data = Category.by_id(id)
    if request.method == "GET":
        form.pid.data = data.pid
        form.name.data = data.name
        form.keywords.data = data.keywords
        form.status.data = data.status
        form.sort.data = data.sort
        form.description.data = data.description
        return render_template('admin/category/edit.html', form=form, data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.update(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/category/category_stop/<int:id>', methods=['GET'])
@require_login
def admin_category_stop(id):
    if request.method == "GET":
        category = Category.by_id(id)
        category.status = 2
        result = Category.change_status(category)
        return jsonify(result)


@admin.route('/category/category_start/<int:id>', methods=['GET'])
@require_login
def admin_category_start(id):
    if request.method == "GET":
        category = Category.by_id(id)
        category.status = 1
        result = Category.change_status(category)
        return jsonify(result)
