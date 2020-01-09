#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/10/14.
from app.frontend import frontend
from app.modules.Category import Category
from app.modules.Posts import Posts
from app.utils.category import to_level


@frontend.context_processor
def category():
    """
    导航的分类
    """
    tree = Category.buildTree()
    return dict(tree=tree)


@frontend.context_processor
def hot():
    return dict(hot=Posts.get_hot(1))


@frontend.context_processor
def new_post():
    return dict(new_post=Posts.new_post())
