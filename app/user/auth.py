#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/5/28.
from flask import redirect, flash, url_for, session
from flask_github import GitHub

from app.user import user
from app.utils.user.UserAuth import auth_github
from app.admin.index.dashboard import admin_dashboard

Github = GitHub()


@user.route('/github/callback', methods=['GET'])
@Github.authorized_handler
def github_callback(access_token):
    """
    github回调接口

    :param access_token:
    :return:
    """
    if access_token is None:
        flash('登陆失败')
        return redirect(url_for('user.github'))
    response = Github.get('user', access_token=access_token)
    result = auth_github(response, access_token=access_token)
    if result['status'] is True:
        flash(result['message'], 'ok')
        return redirect('/admin/dashboard')
    else:
        flash(result['message'], 'error')
        redirect(url_for('user.github'))


@user.route('/github/login', methods=['GET'])
def github():
    """
    github第三方登陆 跳转接口
    :return:
    """
    if session.get('user'):
        return redirect('/admin/das')
    return Github.authorize(scope='repo')
