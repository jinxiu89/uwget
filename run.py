#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/11/25.
from werkzeug.contrib.fixers import ProxyFix

from app import create_app
from app.modules import (UserAuths, UserInfo, Category, Posts, Language, PermissionGroup, Permission, Roles, \
                         Relationship)
from app.modules.Base import db

app = create_app('default')
db.init_app(app)
if __name__ == '__main__':
    app.run()
