#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
import time
from .Base import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_base.id"), comment="用户ID，该文章属于那个用户")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), comment="该文章属于哪个分类")
    name = db.Column(db.String(128), comment="文章标题")
    subtitle = db.Column(db.String(64), comment="副标题")
    keywords = db.Column(db.String(128), comment="文章关键词")
    description = db.Column(db.String(255), comment="文章描述")
    title = db.Column(db.String(64), unique=True, comment="文章url")
    content_markdown = db.Column(db.Text, comment="存储markdown文本")
    content_html = db.Column(db.Text, comment="Post内容")
    status = db.Column(db.SmallInteger, comment="状态")
    marked = db.Column(db.SmallInteger, comment='推荐内容')
    clicks = db.Column(db.Integer, default=20, comment='点击阅读数')
    references = db.Column(db.Text, comment="参考文献")
    create_time = db.Column(db.TIMESTAMP, default=int(time.time()), comment='创建时间')
    update_time = db.Column(db.Integer, default=int(time.time()), comment='更新时间')

    def __repr__(self):
        return '<title {}>'.format(self.name)
