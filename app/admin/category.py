#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from app.admin import admin
from flask import render_template, request, jsonify
from forms.category.add import addForm
from app.modules.Category import Category


@admin.route('/category', methods=['GET'])
def admin_category_list():
    if request.method == 'GET':
        return render_template('admin/category/index.html')


@admin.route('/category/add', methods=['GET', 'POST'])
def admin_category_add():
    form = addForm()
    category = [(i.id, i.name) for i in Category.query.all()]
    if not category:
        category.insert(0, (1, "根分类"))
    form.pid.choices = category
    if request.method == "GET":
        return render_template('admin/category/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result = Category.create(data)
            return jsonify(result)
        else:
            for key in form.errors:
                return jsonify({'status': False, 'message': str(form.errors['key'])})
