#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/1.
import uuid
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db
from app.modules.Permission import Permission as Model


class PermissionForm(FlaskForm):
    group_id = SelectField(label="所属组", coerce=int, validators=[], render_kw={
        "class": "select valid",
        "size": 1,
        "style": "height:30px",
    })
    name = StringField(label="权限名称", validators=[DataRequired('权限名称必须输入')], description="权限名称",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "权限名称指某一特定的功能"})
    code = StringField(label="权限码", validators=[DataRequired('权限吗必须填写')], description="权限码是在装饰器中包含的特有编码",
                       render_kw={"id": "code", "class": "input-text size-L", "placeholder": "权限名称指某一特定的功能"})

    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)

    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})

    def create(self):
        data = Model(
            group_id=self.group_id.data,
            name=self.name.data,
            code=self.code.data,
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
        data.group_id = self.group_id.data
        data.code = self.code.data
        data.update_time = int(time.time())
        try:
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': '保存成功'}
        except Exception as e:
            return {'status': False, 'message': str(e)}
