#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from .Base import db
from .Relationship import role_permission


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.relationship('Permissions', secondary=role_permission, lazy='subquery',
                                  backref=db.backref('Roles', lazy=True))
