#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/24.
from app.admin import admin
from flask import render_template, request, jsonify, session
from forms.language.form import Form
from app.modules.Language import Language


@admin.route('/language', methods=['GET', 'POST'])
def admin_language_list():
    if request.method == "GET":
        data, count = Language.all()
        return render_template('admin/language/index.html', data=data, count=count)


@admin.route('/language/add', methods=['GET', 'POST'])
def admin_language_add():
    form = Form()
    if request.method == "GET":
        return render_template('admin/language/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})
