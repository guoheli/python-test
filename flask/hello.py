from flask import Flask

# 实例化Flask对象 app=application
app = Flask(__name__)
# app中的route装饰器  路由
@app.route('/index')
# 和路由绑定的视图函数
def index():
	return 'helloword'	# 相当于Django中的HttpResponse
# 启动服务
app.run()