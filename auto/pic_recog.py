from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()

image = get_file_content('erha.jpg')
""" 如果有可选参数 """
options = {}
options["top_num"] = 1  #返回预测得分top结果数，默认为6
options["baike_num"] = 5    #返回百科信息的结果数，默认不返回

""" 带参数调用动物识别 """
res = client.animalDetect(image, options)

print(res)
