from flask import Flask
from routes import all_blueprints

app = Flask(__name__)

# 注册蓝图
for blueprint in all_blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)
