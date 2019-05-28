#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.admin import admin

db = SQLAlchemy()


def create_app(deploy):
    app = Flask(__name__)
    app.config.from_object(config[deploy])
    config[deploy].init_app(app)
    # db.init_app(app)
    app.register_blueprint(admin)

    # @app.route('/')
    # def main():
    #     return redirect('/')

    return app
