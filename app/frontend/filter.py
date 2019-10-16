#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/14.
from app.frontend import frontend
from app.modules.Category import Category


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
