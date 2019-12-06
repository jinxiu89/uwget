#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
import json
from flask import url_for, session
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, length, Email
from app.modules.UserInfo import UserInfo
from app.modules.UserAuths import UserAuth
from app.modules.Base import db

class LoginForm(FlaskForm):
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
        label="管理员密码",
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
    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       登      录     "})

    def login(self):
        User = db.session.query(UserInfo).filter(UserInfo.email == self.email.data).first()
        if User is None:
            return {'status': False, 'message': '用户不存在'}
        else:
            auth = db.session.query(UserAuth).filter(UserAuth.third_type == 'local', UserAuth.uid == User.id).first()
            if not check_password_hash(auth.access_token,self.password.data):
                return {'status': False, 'message': '输入的密码不正确'}
            else:
                data={'name':User.email,'uuid':'','access':auth.access_token}
                session['user']=json.dumps(data)
                return {'status':True,'message':'登陆成功！'}

