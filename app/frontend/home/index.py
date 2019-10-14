#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/14.
from app.frontend import frontend
from flask import render_template


@frontend.route('/', methods=['GET'])
def frontend_index():
    return render_template('frontend/home/index.html')


@frontend.route('/index', methods=['GET'])
def frontend_index_():
    return render_template('frontend/home/index.html')
