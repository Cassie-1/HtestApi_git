import requests,json

proxies = {'http':'http://localhost:8888'}      #代理
headers={}
headers['Content-Type']='application/json;charset=UTF-8'

http=requests.session()     #得到session运行在整个过程中
resp=http.post(url="http://192.168.1.203:8083/sys/login",
                   proxies=proxies,
                   headers=headers,
                   data='{"userName":"18210034706","password":"123456"}')
resp_dict = json.loads(resp.text)       #json转换成python的dict对象
token = resp_dict['object']['token']
headers['token']=token

data={'token':token}
data_json=json.dumps(data)      #将python对象dict转换成json

resp2=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
                   proxies=proxies,
                   headers=headers,
                   data=data_json
               )

print(resp2.text)
print(resp2.url)
print(resp2.cookies)
print(resp2.headers)
print('http code:%s'%resp2.status_code)