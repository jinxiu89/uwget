#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 2019/8/17.


def packing_error(errors):
    """
    本函数用于包装form传过来的错误信息，因为这一段如果不抽出来，会重复写很多遍
    使用的地方均为路由的错误异常的地方例如
    @admin.route('/category/add', methods=['GET', 'POST'])
def category_add():
    form = Form()
    form.pid.choices = Category.choices()
    if request.method == "GET":
        return render_template('admin/category/add.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result = Category.create(data)
            return jsonify(result)
        else:
            error = packing_error(form.errors)
            return jsonify({'status': False, 'message': str(error)})
    :param errors: 是form.errors
    :return: 返回所有的错误
    """
    error = []
    for value in errors.values():
        error.append(value[0])
    return error
