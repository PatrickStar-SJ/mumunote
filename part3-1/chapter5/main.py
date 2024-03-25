import os
from flask import Flask, make_response, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24) # 生成随机种子，用于生成sessionid

@app.route("/login")
def login():
    session["islogin"] = True
    return"登录成功"

@app.route("/update_user")
def update_user():
    return"修改用户信息成功"

#全局拦截器,不管请求的url是什么，都会先执行这个函数
@app.before_request
def before():

    # 拦截器，如果用户没有登录，则跳转到登录页面
    url = request.path
    print(url)

    # 定义白名单
    pass_path = ['/', '/login']
    #定义一个可通过的后缀名
    suffix = url.endswith("png") or url.endswith("jpg") or url.endswith("css") or url.endswith("js")


    if url in pass_path or suffix:
        pass
    else:
        # 判断用户是否登录
        if not session.get("islogin"):
            return "请登录"

        



if __name__ == "__main__":
    app.run(debug=True)