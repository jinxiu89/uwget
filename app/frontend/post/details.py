#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/16.
from app.frontend import frontend
from flask import render_template, request
from app.modules.Posts import Posts
from app.forms.posts.form import Comment


@frontend.route('/post/<string:title>.html', methods=['GET'])
def frontend_post_details(title):
    form = Comment()
    if request.method == 'GET':
        result = Posts.by_title(title)
        return render_template('frontend/post/details.html', result=result, form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})
