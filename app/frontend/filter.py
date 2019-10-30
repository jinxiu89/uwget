#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/14.
from app.frontend import frontend
from app.modules.Category import Category
from app.modules.Posts import Posts


@frontend.app_template_filter('getTags')
def get_parent(keywords):
    """
    连接还没有处理好
    :param keywords:
    :return:
    """
    keyword = keywords.split(',')
    tags = ''
    for i in keyword:
        tags += '<li><a href="/post/{}">{}</a></li>'.format(i, i)
    return tags


@frontend.app_template_filter('getCategoryName')
def get_category_name(id):
    """
    根据category_id来获取分类名
    :param id:
    :return:
    """
    data = Category.by_id(id)
    return data.name


@frontend.app_template_filter('getCategoryTitle')
def get_category_title(id):
    data = Category.by_id(id)
    return data.title


@frontend.app_template_filter('prevPost')
def prev_post(id):
    data = Posts.by_id(id - 1)
    if data is not None:
        return "<a href=\"/post/{}.html\" target=\"_blank\">{}</a>".format(data.title, data.name)
    return "无"


@frontend.app_template_filter('nextPost')
def next_post(id):
    data = Posts.by_id(id + 1)
    if data is not None:
        return "<a href=\"/post/{}.html\" target=\"_blank\">{}</a>".format(data.title, data.name)
    return "无"
