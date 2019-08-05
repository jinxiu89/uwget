#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
from .Base import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), comment="分类名称")
    title = db.Column(db.String(64), comment="url标识")
    keywords = db.Column(db.String(128), comment="分类关键词")
    list_order = db.Column(db.Integer, comment="列表排序")
    status = db.Column(db.SmallInteger, comment="状态")
    description = db.Column(db.String(255), comment="分类描述")

    def __repr__(self):
        data = {"name": self.name, "title": self.title}
        return '{}'.format(data)
