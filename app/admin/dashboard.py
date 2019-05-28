#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from app.admin import admin


@admin.route('/dashboard', methods=['GET'])
def admin_dashboard():
    return 'hello admin dashboard'
