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

    @classmethod
    def change_status(cls, data):
        try:
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': "成功！"}
        except Exception as e:
            return {'status': False, 'message': str(e)}
