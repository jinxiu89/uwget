#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from app.admin import admin


@admin.route('user/login', methods=['GET', 'POST'])
def admin_login():
    pass


@admin.route('/user/logout', methods=['GET', 'POST'])
def admin_logout():
    pass
