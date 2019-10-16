#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_moment import Moment
from app.modules.Base import db
from config import config
from app.admin import admin
from app.user import user
from app.user.auth import Github
from app.frontend import frontend

csrf = CSRFProtect()
moment = Moment()

# csrf.exempt(user) 如果要把某个蓝图忽略掉 csrf ，这一般在API接口上非常游泳


def create_app(deploy):
    app = Flask(__name__)
    app.config.from_object(config[deploy])
    config[deploy].init_app(app)
    db.init_app(app)
    csrf.init_app(app=app)
    Github.init_app(app)
    moment.init_app(app)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    @app.errorhandler(CSRFError)
    def csrf_error(reason):
        return render_template('csrf_error.html', reason=reason)

    return app
