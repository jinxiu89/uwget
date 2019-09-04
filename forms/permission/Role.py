#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/4.
import uuid
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db


class RoleForm(FlaskForm):
    name = StringField(label="角色名称", validators=[DataRequired('名称必须输入')], description="角色名称",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "按照网站功能来切分角色"})

    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})
