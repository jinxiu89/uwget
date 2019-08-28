#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/28.
import time
from .Base import db


class PermissionGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment="组ID")
    name = db.Column(db.String(16), comment="组名")
    create_time = db.Column(db.Integer, default=int(time.time()), comment="创建时间")
    update_time = db.Column(db.Integer, default=int(time.time()), comment="更新时间")
    permission = db.relationship("Permission", backref="group", lazy="dynamic")

    def __repr__(self):
        data = {"name": self.name}
        return '{}'.format(data)
