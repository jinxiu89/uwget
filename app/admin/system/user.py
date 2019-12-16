#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/12/16.
from app.admin import admin
from flask import render_template, request, jsonify, session


@admin.route('/user/list', methods=['GET'])
def admin_user_list():
    if request.method == "GET":
        return render_template('admin/user/index.html')
