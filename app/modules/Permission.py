#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/28.
import time
from .Base import db


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment="权限ID")
    group_id = db.Column(db.Integer, db.ForeignKey("permission_group.id"), comment="权限组")
    name = db.Column(db.String(16), comment="权限名称")
    code = db.Column(db.String(32), comment="权限码")
    create_time = db.Column(db.Integer, default=int(time.time()), comment="创建时间")
    update_time = db.Column(db.Integer, default=int(time.time()), comment="更新时间")

    def __repr__(self):
        data = {"name": self.name, "code": self.code}
        return '{}'.format(data)

    @classmethod
    def all(cls):
        query = db.session.query(cls)
        data = query.order_by(cls.id.asc()).all()
        count = query.count()
        return data, count

    @classmethod
    def by_id(cls, id):
        return db.session.query(cls).filter_by(id=id).first()
