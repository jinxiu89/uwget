#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/31.
from functools import wraps
from flask import session, redirect, url_for, request, flash


def require_login(function):
    @wraps(function)
    def req(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('user.login', next=request.url))
        return function(*args, **kwargs)

    return req
