#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/14.
from app.frontend import frontend
from flask import render_template
from app.modules.Posts import Posts


@frontend.route('/', methods=['GET'])
def frontend_index():
    data, count = Posts.all()
    return render_template('frontend/home/index.html', data=data, count=count)


@frontend.route('/index', methods=['GET'])
def frontend_index_():
    return render_template('frontend/home/index.html')
