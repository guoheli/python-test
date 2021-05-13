import requests, json
github_url = "http://127.0.0.1:9999/get_json?name=tttt&age=20"
data = json.dumps({'name':'test', 'description':'some test repo'})
r = requests.get(github_url)
print(r.json())