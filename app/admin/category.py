#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from app.admin import admin
from flask import render_template, request, jsonify
from forms.category.form import Form
from app.modules.Category import Category
from utils.admin.common import packing_error


@admin.route('/category', methods=['GET'])
def category_list():
    if request.method == 'GET':
        data, count = Category.all()
        return render_template('admin/category/index.html', data=data, count=count)


@admin.route('/category/add', methods=['GET', 'POST'])
def category_add():
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
def category_edit(id):
    form = Form()
    form.pid.choices = Category.choices()
    if request.method == "GET":
        data = Category.by_id(id)
        form.pid.data = data.pid
        form.name.data = data.name
        form.keywords.data = data.keywords
        form.status.data = data.status
        form.sort.data = data.sort
        form.description.data = data.description
        return render_template('admin/category/edit.html', form=form, data=data)
    if request.method == "POST":
        category = Category.by_id(id)
        if form.validate_on_submit():
            result = form.update(category)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/category/category_stop/<int:id>', methods=['GET'])
def category_stop(id):
    if request.method == "GET":
        category = Category.by_id(id)
        category.status = 2
        result = Category.change_status(category)
        return jsonify(result)


@admin.route('/category/category_start/<int:id>', methods=['GET'])
def category_start(id):
    if request.method == "GET":
        category = Category.by_id(id)
        category.status = 1
        result = Category.change_status(category)
        return jsonify(result)
