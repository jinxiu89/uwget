#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/11.
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, length, Email


class addForm(FlaskForm):

    pid = StringField(label="根分类", coerce=int, validators=[DataRequired('请选择父分类')], render_kw={
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
    description = TextAreaField(label="描述", validators=[DataRequired('描述必须填'), length(10, 64, "描述不能超过64个字符")],
                                description="描述",
                                render_kw={"id": "description", "class": "textarea description-textarea",
                                           "cols": "", "rows": "",
                                           "placeholder": "描述是seo的关键信息，请想好后添加，也可以先填一个，后期再修改"})
    submit = SubmitField(render_kw={"class": "btn btn-primary radius size-L", "value": "提交"})
