#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
from .Base import db

import time
import uuid


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, comment="父分类ID")
    name = db.Column(db.String(64), comment="分类名称")
    title = db.Column(db.String(64), comment="url标识")
    keywords = db.Column(db.String(128), comment="分类关键词")
    sort = db.Column(db.Integer, comment="列表排序")
    status = db.Column(db.SmallInteger, comment="状态")
    description = db.Column(db.String(255), comment="分类描述")
    create_time = db.Column(db.Integer, comment="创建时间")

    def __repr__(self):
        data = {"name": self.name, "title": self.title}
        return '{}'.format(data)

    @classmethod
    def all(cls):
        """

        :return:
        """
        query = db.session.query(cls)
        data = query.all()
        count = query.count()
        return data, count

    @classmethod
    def choices(cls):
        category = [(i.id, i.name) for i in cls.query.all()]
        category.insert(0, (0, "根分类"))
        return category

    @classmethod
    def by_id(cls, id):
        """
        根据ID 查询单条数据
        :param id:
        :return:
        """
        return db.session.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, name):
        """
        根据name查询
        :param name:
        :return:
        """
        return db.session.query(cls).filter_by(name=name).first()

    @classmethod
    def change_status(cls, category):
        try:
            db.session.add(category)
            db.session.commit()
            return {'status': True, 'message': "成功！"}
        except Exception as e:
            return {'status': False, 'message': str(e)}
