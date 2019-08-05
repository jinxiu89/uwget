#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/6/23.
from redis import Redis
from config import REDIS_OPTIONS

redis = Redis(**REDIS_OPTIONS)


def get_redis_data(key):
    return redis.get(key)


def set_redis_data(key, value):
    redis.set(name=key, value=value, ex=600)
