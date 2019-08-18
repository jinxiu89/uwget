#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from .Base import db
from .UserAuths import UserAuth
import json


class UserBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), comment='用户名')  # name
    avatar_url = db.Column(db.String(255))
    password = db.Column(db.String(255), comment='密码')
    email = db.Column(db.String(64), comment='邮箱')
    phone = db.Column(db.String(11), comment='手机')
    name = db.Column(db.String(64), comment='真实姓名')
    nickname = db.Column(db.String(64), comment='用户昵称')
    gender = db.Column(db.SmallInteger(), comment='性别')
    city = db.Column(db.String(16), comment='城市')
    company = db.Column(db.String(32), comment='公司')
    title = db.Column(db.String(32), comment='头衔，职位')
    website = db.Column(db.String(128), comment='个人网站，博客')
    description = db.Column(db.Text, comment='个人简介')
    signature = db.Column(db.String(255), comment='个人签名')
    user_auth = db.relationship('UserAuth', backref="user", lazy='dynamic')
    posts = db.relationship('Posts', backref="user", lazy="dynamic")

    def __repr__(self):
        data = {"name": self.name, "uuid": self.uuid}
        return '{}'.format(data)

    @classmethod
    def by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()

    @classmethod
    def by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def create(cls, User):
        db.session.add(User)
        db.session.commit()
        return True
