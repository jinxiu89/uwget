#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/18.
from app.admin import admin
from flask import render_template, request, jsonify, session
from forms.posts.form import Form
from app.modules.Category import Category
from app.modules.Posts import Posts


@admin.route('/posts', methods=['GET'])
def admin_posts_list():
    data, count = Posts.all()
    return render_template('admin/posts/index.html', data=data, count=count)


@admin.route('/post/add', methods=['GET', 'POST'])
def admin_post_add():
    form = Form()
    form.category_id.choices = Category.choices()
    if request.method == "GET":
        return render_template('admin/posts/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            result = form.create()
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})


@admin.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def admin_post_edit(id):
    form = Form()
    form.category_id.choices = Category.choices()
    data = Posts.by_id(id)
    if request.method == "GET":
        form.category_id.data = data.category_id
        form.name.data = data.name
        form.subtitle.data = data.subtitle
        form.keywords.data = data.keywords
        form.description.data = data.description
        form.markdown.data = data.markdown
        form.markdown_html_code.data = data.markdown_html_code
        form.marked.data = data.marked
        form.status.data = data.status
        form.references.data = data.references
        return render_template('admin/posts/edit.html', form=form, data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            if form.validate_on_submit():
                result = form.update(data)
                return jsonify(result)
            else:
                error = packing_error(form.errors)
                return jsonify({'status': False, 'message': str(error)})
