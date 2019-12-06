#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
import uuid
from werkzeug.security import generate_password_hash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, length, Email, equal_to
from app.modules.Base import db
from app.modules.UserInfo import UserInfo
from app.modules.UserAuths import UserAuth


class RegForm(FlaskForm):
    email = StringField(
        label="邮箱",
        validators=[DataRequired('请输入用户邮箱')],
        description="邮箱",
        render_kw={
            "id": "email",
            "class": "input-text size-L",
            "placeholder": "jinxiu89@163.com"
        }
    )
    password = StringField(
        label="输入密码",
        validators=[DataRequired("请输入密码")],
        description="密码",
        render_kw={
            "type": "password",
            "class": "input-text size-L",
            "id": "password",
            "autocomplete": "off",
            "placeholder": "密码"
        }
    )
    repassword = StringField(
        label="重输密码",
        validators=[DataRequired("请输入密码")],
        description="验证密码",
        render_kw={
            "type": "password",
            "class": "input-text size-L",
            "id": "repassword",
            "autocomplete": "off",
            "placeholder": "重输密码"
        }

    )
    submit = SubmitField(
        render_kw={"class": "btn button btn-primary btn-block radius size-L", 'type': 'button',
                   "value": "       注      册     "})

    def create(self):
        User = db.session.query(UserInfo).filter(UserInfo.email == self.email.data).first()
        if User is None:
            user = UserInfo(
                email=self.email.data,
                uuid=uuid.uuid4().hex[0:16:2]
            )
            user.user_auth = [UserAuth(third_type='local',
                                       access_token=generate_password_hash(self.password.data))]
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {'status': False, 'message': str(e)}
            return {'status': True, 'message': "注册成功"}
        else:
            return {'status': False, 'message': "不能注册！"}
