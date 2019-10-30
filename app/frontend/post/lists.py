#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/30.
from app.frontend import frontend
from flask import render_template
from app.modules.Posts import Posts
from app.modules.Category import Category


@frontend.route('/post/category/<string:title>.html', methods=['GET'])
def frontend_post_list(title):
    category = Category.by_category_title(title)
    result, count = Posts.by_category(category.id)
    return render_template('frontend/post/lists.html', data=result, count=count)
