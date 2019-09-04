#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.modules.Base import db
from app.modules import (UserAuths, UserBase, Category, Posts, Language, PermissionGroup, Permission, Roles,\
                         Relationship)


app = create_app('default')





migrate = Migrate(app, db)
manger = Manager(app)
manger.add_command("db", MigrateCommand)
if __name__ == '__main__':
    manger.run()
