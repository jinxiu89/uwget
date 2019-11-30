#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from app.user import user
from flask import render_template, request
from forms.user.login import LoginForm
from forms.user.reg import RegForm
from libs.redis import set_redis_data


@user.route('/login', methods=['GET', 'POST'])
def login():
    # set_redis_data('name', 'qiu jin')
    form = LoginForm()
    if request.method == 'GET':
        return render_template('user/login.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.data
            print(data)


@user.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'GET':
        return render_template('user/reg.html', message="用户注册", form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.data


@user.route('/logout', methods=['GET', 'POST'])
def logout():
    pass
