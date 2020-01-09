#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/31.


class Classify:

    @staticmethod
    def toLevel(cate, delimiter='-', pid=0, level=1):
        arr = []
        for i in cate:
            print(type(i))
            # if i['pid'] == pid:
            #     i['level'] = level + 1
            #     i['delimiter'] = delimiter * level
            #     arr.append(i)
            #     arr = toLevel(cls, cate, delimiter, i['id'], v['level'])

        return arr
