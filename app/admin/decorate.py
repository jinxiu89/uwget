#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/31.
from functools import wraps
from flask import session, redirect, url_for, request, flash


def is_login(f):
    """
    强制登录装饰器，检查所有的连接是否在登录状态
    :param f:
    :return:
    """
    @wraps(f)
    def req(*args, **kwargs):
        if session.get("user") is None:
            return redirect(url_for("user.login", next=request.url))
        return f(*args, **kwargs)

    return req
