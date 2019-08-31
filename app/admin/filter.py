#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/31.
from app.admin import admin


@admin.app_template_filter('getParent')
def get_parent(id):
    from app.modules.Category import Category
    category = Category.by_id(id)
    if category is None:
        return "根分类"
    return category.name
