#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/24.
from app.admin import admin
from flask import render_template


@admin.route('/language', methods=['GET', 'POST'])
def admin_language_list():
    return render_template('admin/language/index.html')
