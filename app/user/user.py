#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from app.user import user
from flask import render_template, request, redirect, url_for, jsonify, session, flash
from forms.user.login import LoginForm
from forms.user.reg import RegForm
from libs.redis import set_redis_data
from utils.admin.common import packing_error


@user.route('/login', methods=['GET', 'POST'])
def login():
    if session.get("user") is not None:
        return redirect(url_for("admin.admin_dashboard"))
    else:
        form = LoginForm()
        if request.method == 'GET':
            return render_template('user/login.html', form=form)
        if request.method == 'POST':
            if form.validate_on_submit():
                result = form.login()
                result['next'] = '/admin/dashboard'
                return jsonify(result)
            else:
                error = packing_error(form.errors)
                return jsonify({'status': False, 'message': str(error)})


@user.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'GET':
        return render_template('user/reg.html', message="用户注册", form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            result = form.create()
            result['next'] = url_for('user.login')
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@user.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop("user", None)
    flash("成功退出！", "ok")
    return redirect(url_for("user.login"))
