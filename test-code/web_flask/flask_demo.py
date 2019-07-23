#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/7/17 11:50
@Desc   ：
=================================================='''
from flask import Flask
from flask import jsonify
from flask import request, Response
from flask_restful import reqparse, abort, Api, Resource
import random
import time

# 初始化
app = Flask(__name__)
api = Api(app)


# 生成随机字符串
def random_str(lenght):
    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

    # 用时间来做随机播种
    random.seed(time.time())
    time.sleep(0.1)

    # 随机选取数据
    sa = []
    for i in range(lenght):
        sa.append(random.choice(data))
    salt = ''.join(sa)

    return salt


# 初始化源数据
# 随机生成
USERS = {
    "user1": {
        "username": random_str(10),
        "password": random_str(16),
        "token": random_str(32)
    },
    "user2": {
        "username": random_str(10),
        "password": random_str(16),
        "token": random_str(32)
    },
    "user3": {
        "username": random_str(10),
        "password": random_str(16),
        "token": random_str(32)
    }
}


# 判断用户id是否存在
def abort_if_user_not_exist(user_id):
    if user_id not in USERS:
        abort(404, message="user {%s} is not exist" % user_id)


parser = reqparse.RequestParser()
parser.add_argument("username", type=str)


# 用户管理
class User(Resource):
    # 获取指定用户信息
    def get(self, user_id):
        abort_if_user_not_exist(user_id)

        return USERS[user_id]

    # 删除指定用户
    def delete(self, user_id):
        abort_if_user_not_exist(user_id)

        del USERS[user_id]

        return "", 204

    # 新增/修改用户
    def put(self, user_id):
        args = parser.parse_args()
        print(args)

        user = {"username": args["username"],
                "password": random_str(16),
                "token": random_str(32)}

        USERS[user_id] = user

        return user, 201

    # 新增/修改用户
    def post(self, user_id):
        args = parser.parse_args()
        print(args)
        user = {"username": args["username"],
                "password": random_str(16),
                "token": random_str(32)}

        USERS[user_id] = user

        return user, 201


# 查询所有用户信息
class UserList(Resource):
    def get(self):
        return USERS


# 新增资源
api.add_resource(UserList, "/user")
api.add_resource(User, "/user/<user_id>")


@app.route('/index')
def index():
    return 'Index Page'


# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())

    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'

    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username=random_str(),
        password=random_str()
    )


# http POST
@app.route("/update", methods=["POST"])
def update():
    return make_response()


# http delete
@app.route("/delete", methods=["DELETE"])
def delete():
    return make_response()


# http head
@app.route("/head", methods=["HEAD"])
def head():
    return make_response()


if __name__ == "__main__":
    app.debug = True  # 开启调试模式,它 绝对不能用于生产环境
    # app.run(host='0.0.0.0')  # 让外部也能访问的务器，添加host='0.0.0.0'
    print(USERS.keys())
    app.run()
