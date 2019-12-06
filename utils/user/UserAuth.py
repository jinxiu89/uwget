#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/27.
import json
from app.modules.UserInfo import UserInfo
from app.modules.UserAuths import UserAuth as userAuth
from app.modules.Base import db
from flask import session


def auth_github(response, access_token):
    User = db.session.query(UserInfo).filter(UserInfo.uuid == response['id']).first()
    if User is None:
        # 注册一个
        User = UserInfo(
            uuid=response['id'],
            username=response['login'],
            email=response['email'],
            name=response['name'],
            avatar_url=response['avatar_url']
        )
        User.user_auth = [userAuth(
            third_type='github',
            access_token=access_token
        ), ]
        db.session.add(User)
        db.session.commit()
        data = {
            'name': response['login'],
            'uuid': response['id'],
            'access': access_token
        }
        session['user'] = json.dumps(data)
        return {'status': True, 'message': "登陆成功"}

    else:
        db.session.query(userAuth).filter(userAuth.third_type == 'github', userAuth.uid == User.id).update(
            {"access_token": access_token})
        db.session.commit()
        data = {
            'name': response['login'],
            'uuid': response['id'],
            'access': access_token
        }
        session['user'] = json.dumps(data)
        return {'status': True, 'message': "登陆成功"}
