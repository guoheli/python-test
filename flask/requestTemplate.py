from flask import Flask, send_file, jsonify, render_template, request
app = Flask(__name__)
@app.route('/get_file')
def get_file():
    # 返回helloword.py里的内容  Content-Type: text/plain; charset=utf-8
	# return send_file('helloword.py')
	# 返回图片  Content-Type: image/jpeg
	return send_file('1.png')
	# 返回MP4 或 MP3   Content-Type: voide/mp4
    # return send_file('2.mp4')
	# 下载 这个exe文件  Content-Type: application/x-msdownload
	# return send_file('3.exe')
# 启动服务

@app.route("/get_json")
def get_json():
    name = request.args.get("name", 0)
    age = request.args.get("age", 0)
    dic = { "name": name, "age": age}
    return jsonify(dic)



@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.run("0.0.0.0", 9999)