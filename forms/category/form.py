#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
import uuid
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db
from app.modules.Category import Category


class Form(FlaskForm):
    """
    wtforms:每一个功能一个form,
    """
    pid = SelectField(label="根分类", coerce=int, validators=[], render_kw={
        "class": "select valid",
        "size": 1,
        "style": "height:30px",
    })
    name = StringField(label="分类名", validators=[DataRequired('分类名必须输入')], description="分类名",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "分类名可以是话题名，技术栏目等"})
    keywords = StringField(label="关键词", validators=[DataRequired('关键词必须填'), length(10, 64, "关键词不能超过64个字符和少于10个字符")],
                           description="关键词",
                           render_kw={"id": "keywords", "class": "input-text size-L",
                                      "placeholder": "关键词是seo的关键信息，请想好后添加，也可以先填一个，后期再修改"})
    status = RadioField(label="状态", validators=[DataRequired("状态必须选择一个")], coerce=int, choices=((1, '启用'), (2, '禁用')),
                        render_kw={
                            "class": "radio-box"
                        })
    description = TextAreaField(label="描述", validators=[DataRequired('描述必须填'), length(10, 64, "描述不能超过64个字符")],
                                description="描述",
                                render_kw={"id": "description", "class": "textarea description-textarea",
                                           "cols": "", "rows": "",
                                           "placeholder": "描述是seo的关键信息，请想好后添加，也可以先填一个，后期再修改"})
    sort = IntegerField(label='排序', validators=[DataRequired("排序必须填写")], description="排序",
                        render_kw={"id": "sort", "class": "input-text size-L", "placeholder": 100})

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

    submit = SubmitField(render_kw={"class": "button btn btn-primary radius size-L", 'type': 'button', "value": "提交"})

    def create(self):
        """
        根新和新增为什么放在form里做呢？
        因为方便，符合flask-wtforms 的设计逻辑，理应如此
        """
        result = Category(
            pid=self.pid.data,
            name=self.name.data,
            title='c'+uuid.uuid4().hex[0:16:2],
            keywords=self.keywords.data,
            sort=self.sort.data,
            status=self.status.data,
            description=self.description.data,
            create_time=datetime.utcnow()
        )
        try:
            db.session.add(result)
            db.session.commit()
            return {'status': True, 'message': "创建成功"}
        except Exception as e:
            db.session.rollback()
            return {'status': False, 'message': str(e)}

    def update(self, category):
        """
        根新和新增为什么放在form里做呢？
        因为方便，符合flask-wtforms 的设计逻辑，理应如此
        """
        try:
            category.name = self.name.data
            category.pid = self.pid.data
            category.keywords = self.keywords.data
            category.sort = self.sort.data
            category.status = self.status.data
            category.description = self.description.data
            category.update_time = datetime.utcnow()
            db.session.add(category)
            db.session.commit()
            return {'status': True, 'message': "保存成功"}
        except Exception as e:
            db.session.rollback()
            return {'status': False, 'message': str(e)}
