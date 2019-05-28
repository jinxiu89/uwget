#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask_script import Manager, Shell
from app import create_app, db

app = create_app('default')
manger = Manager(app)
# def make_shell_context():
#     return dict(app=app,)
# manger.add_command()

if __name__ == '__main__':
    manger.run()
