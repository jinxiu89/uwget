#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
import json
from .Base import db
from .Posts import Posts  # 关系表，分文件存储表时，需要 import
from flask import jsonify, url_for
from utils.category import to_level


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, comment="父分类ID")
    name = db.Column(db.String(64), comment="分类名称")
    title = db.Column(db.String(64), comment="url标识")
    keywords = db.Column(db.String(128), comment="分类关键词")
    sort = db.Column(db.Integer, comment="列表排序")
    status = db.Column(db.SmallInteger, comment="状态")
    level = db.Column(db.Integer, comment="分类级别")
    is_directory = db.Column(db.Integer, comment="判断是否是父级，只要有下一级就是父级")
    path = db.Column(db.String(64), comment="用于查询出子分类的文章")
    description = db.Column(db.String(255), comment="分类描述")
    create_time = db.Column(db.Integer, comment="创建时间")
    posts = db.relationship("Posts", backref="category", lazy="dynamic")

    def __repr__(self):
        data = {
            "id": self.id,
            "pid": self.pid,
            "level": self.level,
            "path": self.path,
            "name": self.name,
            "title": self.title
        }
        return '{}'.format(data)

    @classmethod
    def all(cls):
        """

        :return:
        """
        query = db.session.query(cls)
        data = query.order_by(cls.pid.asc(), cls.id.asc()).all()
        count = query.count()
        return data, count

    @classmethod
    def by_status(cls):
        return cls.query.filter_by(status=1).all()

    @classmethod
    def choices(cls):
        category = [(i.id, i.name) for i in cls.query.all()]
        category.insert(0, (0, "根分类"))
        return category

    @classmethod
    def toLayer(cls):
        """
        这段代码是为zTree的数据结构设计的，根据ztree 的结构，将其设计为{}格式，这里卡了好久，但是是值得的，拥有解困能力 才是更重要的，善于分析
        :return:json数据
        """
        category = [{'id': i.id, 'pid': i.pid, 'name': i.name, 'title': i.title,
                     'url': url_for('admin.admin_post_category_list', category_id=i.id), 'target': '_self'} for i in
                    cls.query.all()]
        return category

    @classmethod
    def buildTree(cls):
        lists = [{'id': item.id, 'pid': item.pid, 'name': item.name, 'title': item.title} for item in
                 cls.query.filter_by(status=1).all()]
        return to_level(lists, 0, 0)

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
    def by_category_title(cls, title):
        return db.session.query(cls).filter_by(title=title).first()

    @classmethod
    def change_status(cls, category):
        try:
            db.session.add(category)
            db.session.commit()
            return {'status': True, 'message': "成功！"}
        except Exception as e:
            return {'status': False, 'message': str(e)}
