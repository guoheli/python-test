from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

face_client = AipFace(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


bytes_str = base64.b64encode(get_file_content('people/1.jpg'))
image = str(bytes_str, "utf8")

imageType = "BASE64"

options = {}
options["face_field"] = "age,beauty"
""" 调用人脸检测 """
res = face_client.detect(image, imageType, options)

age = res.get("result").get("face_list")[0].get("age")
beauty = res.get("result").get("face_list")[0].get("beauty")
print(f"年龄：{age}岁", f"颜值：{beauty}分")