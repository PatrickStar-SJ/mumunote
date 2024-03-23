from flask import Flask, make_response, request
import datetime

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return "flask我又来啦"

# 设置cookie
@app.route("/cookie")
def cookie():
    response = make_response("设置cookie成功")
    # 设置cookie
    # response.set_cookie('name', 'zhangsan',max_age=3) # 设置3秒过期

    # 设置1天过期
    expires_time = datetime.datetime.now() + datetime.timedelta(days=1)
    response.set_cookie("name", "dazhoulaoshi",expires=expires_time)
    response.set_cookie("height", "180",expires=expires_time)
    response.set_cookie("sex", "man",expires=expires_time)


    return response


# 获取cookie
@app.route("/get_cookie")
def get_cookie():
    name = request.cookies.get("name")
    print(name)

    cookies = request.cookies
    print(cookies)
    cookies_dict = request.cookies.to_dict()
    print(cookies_dict)

    return"获取cookie成功"


@app.route("/delete_cookie")
def delete_cookie():
    response=make_response("删除cookie成功")
    response.delete_cookie("name")
    cookies_dict = request.cookies.to_dict()
    print(cookies_dict)
    for k, v in cookies_dict.items:
        print(k, v)
        response.delete_cookie(k)
    return response


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()

