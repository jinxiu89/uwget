#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, length
from app.modules.Category import Category


class addForm(FlaskForm):
    pid = SelectField(label="根分类", coerce=int, validators=[DataRequired('请选择父分类')], render_kw={
        "class": "select valid",
        "size": 1,
        "style": "height:30px",
    })
    name = StringField(label="分类名", validators=[DataRequired('分类名必须输入')], description="分类名",
                       render_kw={"id": "name", "class": "input-text size-L", "placeholder": "分类名可以是话题名，技术栏目等"})
    keywords = StringField(label="关键词", validators=[DataRequired('关键词必须填'), length(10, 64, "关键词不能超过64个字符")],
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

    def __init__(self, *args, **kwargs):
        super(addForm, self).__init__(*args, **kwargs)

    submit = SubmitField(render_kw={"class": "btn btn-primary radius size-L", "value": "提交"})

    def create(self):
        Category.create(self)

