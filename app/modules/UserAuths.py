#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from .Base import db


class UserAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user_info.id'))  # user base 表中的 id字段
    third_type = db.Column(db.String(64))  # 三方登陆类型
    access_token = db.Column(db.String(255))  # 令牌 密码

    def __repr__(self):
        return '<access_token %r>' % self.access_token

    @classmethod
    def by_uuid(cls, uid):
        pass
