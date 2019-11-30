#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/11/9.


def to_level(data, pid=0, level=0):
    tree = []
    for item in data:
        if item['pid'] == pid:
            item['level'] = level
            child = to_level(data, item['id'], level + 1)
            item['child'] = []
            if child:
                item['child'] += child
            tree.append(item)
    return tree

