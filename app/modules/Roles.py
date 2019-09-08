#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
import time
from .Base import db
from .Relationship import role_permission
from .Permission import Permission


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    create_time = db.Column(db.Integer, default=int(time.time()), comment="创建时间")
    update_time = db.Column(db.Integer, default=int(time.time()), comment="更新时间")
    permissions = db.relationship('Permission', secondary=role_permission, lazy='subquery',
                                  backref=db.backref('Roles', lazy=True))

    def __repr__(self):
        data = {"name": self.name, "create time": self.create_time, "update time": self.update_time}
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
