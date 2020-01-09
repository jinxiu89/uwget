#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/9/4.
import time

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from app.modules.Base import db
from app.modules.Roles import Roles


class RoleForm(FlaskForm):
    name = StringField(label="角色名称", validators=[DataRequired('名称必须输入')], description="角色名称",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "按照网站功能来切分角色"})

    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})

    def create(self):
        data = Roles(
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
