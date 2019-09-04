#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/4.
from .Base import db

role_permission = db.Table('role_permission',
                           db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
                           db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
                           )
