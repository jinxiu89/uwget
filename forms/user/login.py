#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, length, Email


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
