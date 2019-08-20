#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/20.
import uuid
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, length
from app.modules.Base import db


# from app.modules.Category import Category

class Form(FlaskForm):
    category_id = SelectField(label="所属分类", coerce=int, validators=[], render_kw={
        "class": "select valid",
        "size": 1,
        "style": "height:30px",
    })

    name = StringField(label="文章标题", validators=[DataRequired('文章标题必须输入')], description="文章标题",
                       render_kw={"id": "name", "class": "input-text size-L",
                                  "placeholder": "文章标题可以是话题名，SEO非常重要"})

    subtitle = StringField(label="副标题", validators=[length(8, 64)], description="副标题是配合SEO来使用的",
                           render_kw={"id": "subtitle", "class": "input-text size-L",
                                      "placeholder": "文章副标题，通常是主标题的引申描述"})
    keywords = StringField(label="关键词", validators=[DataRequired('关键词必须填写'), length(8, 64)],
                           description="SEO字段，搜索引擎所属内容",
                           render_kw={"id": "keywords", "class": "input-text size-L",
                                      "placeholder": "关键词，是SEO必备的内容，用于索引本文内容"})
    description = StringField(label="描述", validators=[DataRequired("描述必须填写"), length(8, 255)],
                              description="SEO描述，用于用户搜索查看内容概述",
                              render_kw={"id": "description", "class": "input-text size-L",
                                         "placeholder": "描述，是SEO必备的内容，用于搜索结果也的文章概述"})
    markdown = TextAreaField(label="正文", description="正文",
                             render_kw={"class": "textarea", "rows": "", "cols": "", "placeholder": "100",
                                        "id": "markdown"})
    status = RadioField(label="状态", validators=[DataRequired("状态必须选择一个")], coerce=int, choices=((1, '启用'), (2, '禁用')),
                        render_kw={
                            "class": "radio-box"
                        })
    marked = RadioField(label="推荐", validators=[DataRequired("必须选择一个")], coerce=int, choices=((1, '推荐'), (2, '不推荐')),
                        render_kw={
                            "class": "radio-box"
                        })
    references = TextAreaField(label="参考连接",
                               render_kw={"class": "textarea", "rows": "", "cols": "", "placeholder": "100",
                                          "id": "references"})

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
