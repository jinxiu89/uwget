#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/24.
import time
from .Base import db


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, comment="语言名称")
    code = db.Column(db.String(12), comment="国家简码")
    status = db.Column(db.SmallInteger, comment="状态")
    create_time = db.Column(db.TIMESTAMP, default=int(time.time()), comment="创建时间")
    update_time = db.Column(db.TIMESTAMP, default=int(time.time()), comment="更新时间")

    def __repr__(self):
        data = {"name": self.name, "code": self.code}
        return '{}'.format(data)
