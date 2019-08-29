#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/29.
import uuid
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db
from app.modules.PermissionGroup import PermissionGroup as Model


class PermissionGroup(FlaskForm):
    name = StringField(label="组名称", validators=[DataRequired('组名称必须输入')], description="组名称",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "按功能来分组"})
    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})

    def create(self):
        data = Model(
            name=self.name.data
        )
        try:
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': "创建成功"}
        except Exception as e:
            db.session.rollback()
            return {'status': False, 'message': str(e)}

    def update(self, data):
        data.name = self.name.data
        data.update_time = int(time.time())
        try:
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': '保存成功'}
        except Exception as e:
            return {'status': False, 'message': str(e)}
