#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/12/26.
from .Base import db
from datetime import datetime


class Comments(db.Model):
    """
    评论数据表设计，一问一达，当没有任何@时 to_uid 为空

    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    uid = db.Column(db.Integer, db.ForeignKey('user_info.id'), comment='评论人')
    to_uid = db.Column(db.Integer, default=None, comment='评论哪条评论')
    body = db.Column(db.Text, comment='评论内容')
    body_html = db.Column(db.Text, comment='转化后的评论内容')
    create_time = db.Column(db.DateTime, default=datetime.utcnow(), comment='创建时间')
    status = db.Column(db.Boolean, default=False, comment='评论审核')

    def __repr__(self):
        data = {
            "id": self.id,
            "post_id": self.post_id,
            "uid": self.uid,
            "to_uid": self.to_uid,
            "body": self.body
        }
        return '{}'.format(data)
