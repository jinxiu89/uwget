#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from app.admin import admin
from flask import render_template, request
from forms.category.add import addForm


@admin.route('/category', methods=['GET'])
def admin_category_list():
    if request.method == 'GET':
        return render_template('admin/category/index.html')


@admin.route('/category/add', methods=['GET', 'POST'])
def admin_category_add():
    form = addForm()
    if request.method == 'GET':
        return render_template('admin/category/add.html', form=form)
    if request.method == 'POST':
        pass
