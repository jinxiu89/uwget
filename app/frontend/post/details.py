#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/16.
from app.frontend import frontend
from flask import render_template
from app.modules.Posts import Posts


@frontend.route('/post/<string:title>.html', methods=['GET'])
def frontend_post_details(title):
    result = Posts.by_title(title)
    return render_template('frontend/post/details.html', result=result)