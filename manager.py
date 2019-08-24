#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.modules.Base import db
from app.modules.UserAuths import UserAuth
from app.modules.UserBase import UserBase
from app.modules.Category import Category
from app.modules.Posts import Posts
from app.modules.Language import Language

app = create_app('default')


@app.template_filter('getParent')
def get_parent(id):
    from app.modules.Category import Category
    category = Category.by_id(id)
    if category is None:
        return "根分类"
    return category.name


migrate = Migrate(app, db)
manger = Manager(app)
manger.add_command("db", MigrateCommand)
if __name__ == '__main__':
    manger.run()
