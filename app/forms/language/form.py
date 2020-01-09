#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/25.
import uuid
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db
from app.modules.Language import Language


class Form(FlaskForm):
    name = StringField(label="语言名称", validators=[DataRequired('名称必须输入')], description="语言名称",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "根据国际标准的命名法则来命名"})
    code = StringField(label="Code", validators=[DataRequired('Code必须填')], description="语言code",
                       render_kw={"id": "code", "class": "input-text size-L", "placeholder": "根据国际标准的命名法则来填写"})
    status = RadioField(label="状态", validators=[DataRequired("状态必须选择一个")], coerce=int, choices=((1, '启用'), (2, '禁用')),
                        render_kw={"class": "radio-box"})
    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})

    def create(self):
        result = Language(
            name=self.name.data,
            code=self.code.data,
            status=self.status.data,
        )
        try:
            db.session.add(result)
            db.session.commit()
            return {'status': True, 'message': "创建成功"}
        except Exception as e:
            db.session.rollback()
            return {'status': False, 'message': str(e)}

    def update(self, data):
        try:
            data.name = self.name.data
            data.code = self.code.data
            data.status = self.status.data
            data.update_time = int(time.time())
            db.session.add(data)
            db.session.commit()
            return {'status': True, 'message': "保存成功"}
        except Exception as e:
            return {'status': False, 'message': str(e)}
