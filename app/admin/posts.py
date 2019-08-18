#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/18.
from app.admin import admin
from flask import render_template, request, jsonify


@admin.route('/posts', methods=['GET'])
def posts_list():
    return render_template('admin/posts/index.html')
