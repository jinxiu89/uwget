#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
from datetime import datetime
from .Base import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), db.ForeignKey("user_base.uuid"), comment="用户UUID，该文章属于那个用户")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), comment="该文章属于哪个分类")
    name = db.Column(db.String(128), comment="文章标题")
    subtitle = db.Column(db.String(64), comment="副标题")
    keywords = db.Column(db.String(128), comment="文章关键词")
    description = db.Column(db.String(255), comment="文章描述")
    title = db.Column(db.String(64), unique=True, comment="文章url")
    markdown = db.Column(db.Text, comment="存储markdown文本")
    markdown_html_code = db.Column(db.Text, comment="Post内容")
    status = db.Column(db.SmallInteger, comment="状态")
    marked = db.Column(db.SmallInteger, comment='推荐内容')
    clicks = db.Column(db.Integer, default=20, comment='点击阅读数')
    references = db.Column(db.Text, comment="参考文献")
    create_time = db.Column(db.DateTime, default=datetime.utcnow(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.utcnow(), comment='更新时间')

    def __repr__(self):
        data = {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'create_time': self.create_time
        }
        return '{}'.format(data)

    @classmethod
    def all(cls):
        query = db.session.query(cls)
        data = query.order_by(cls.id.asc(), cls.clicks.desc()).all()
        count = query.count()
        return data, count

    @classmethod
    def by_id(cls, id):
        return db.session.query(cls).filter_by(id=id).first()

    @classmethod
    def by_title(cls, title):
        return db.session.query(cls).filter_by(title=title).first_or_404()

    @classmethod
    def change_status(cls, data):
        try:
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': "处理成功！"}
        except Exception as e:
            return {'status': False, 'message': str(e)}

    @classmethod
    def by_category(cls, category_id):
        query = db.session.query(cls).filter_by(category_id=category_id)
        data = query.order_by(cls.id.asc()).all()
        count = query.count()
        return data, count
