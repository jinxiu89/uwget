#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/12/22.
import uuid
import time
from flask_wtf import FlaskForm


class SettingPermission(FlaskForm):
    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})
