#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/5.
import time
from .Base import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), comment="文章标题")
    title = db.Column(db.String(64), unique=True, comment="文章url")
    keywords = db.Column(db.String(128), comment="文章关键词")
    description = db.Column(db.String(255), comment="文章描述")
    markdown_content = db.Column(db.Text, comment="存储markdown文本")
    content = db.Column(db.Text, comment="Post内容")
    create_time = db.Column(db.TIMESTAMP, default=int(time.time()))
