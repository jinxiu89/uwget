#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/31.
from app.admin import admin
from app.modules.Category import Category
from app.modules.PermissionGroup import PermissionGroup


@admin.context_processor
def to_Layer():
    category = Category.toLayer()
    return dict(category=category)


@admin.context_processor
def permission_group():
    data, count = PermissionGroup.all()
    return dict(permission_group=data)
