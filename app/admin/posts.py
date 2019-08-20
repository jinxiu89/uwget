#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/18.
from app.admin import admin
from flask import render_template, request, jsonify
from forms.posts.form import Form
from app.modules.Category import Category


@admin.route('/posts', methods=['GET'])
def posts_list():
    return render_template('admin/posts/index.html')


@admin.route('/post/add', methods=['GET', 'POST'])
def post_add():
    form = Form()
    form.category_id.choices = Category.choices()
    if request.method == "GET":
        return render_template('admin/posts/add.html', form=form)
