#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/12/16.
from app.admin import admin
from flask import render_template, request, jsonify, session
from app.admin.decorate import require_login


@admin.route('/user/list', methods=['GET'])
@require_login
def admin_user_list():
    if request.method == "GET":
        return render_template('admin/user/index.html')
