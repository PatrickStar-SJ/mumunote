import os
from flask import Flask, make_response, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24) # 生成随机种子，用于生成sessionid

# 注册蓝图
from controller.user import user
app.register_blueprint(user)

from controller.article import article
app.register_blueprint(article)

if __name__ == "__main__":
    app.run(debug=True)