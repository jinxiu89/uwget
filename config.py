#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.

import os

basedir = os.path.abspath(os.path.dirname(__file__))


# os.environ.get() 是获取一个环境变量
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = '879651072@qq.com'
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 部署时要修改转意符号
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/uploads/')
    IMG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/images/")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    HOSTS = '0.0.0.0'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Wavlink@163@localhost/blog'


class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Wavlink@163@localhost/blog'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Wavlink@163@localhost/blog'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
