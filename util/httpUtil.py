# import requests,json
# proxies = {'http':'http://localhost:8888'}
# headers={'Content-Type':'application/json;charset=UTF-8'}
# http=requests.session()
# resp=requests.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    headers=headers,
#                    data='{"userName":"18210034706","password":"123456"}')
# resp_dict = json.loads(resp.text)
# token = resp_dict['object']['token']
# headers['token']=token
# print(resp.text)
# print(resp.url)
# print(resp.cookies)
# print(resp.headers)
# print('http code:%s'%resp.status_code)
# print(resp.encoding)
# print(resp.history)
# print(resp.raw)

import requests,json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def post(self,path,data):
        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)
        if CommonData.token is not None:
            self.headers['token']=CommonData.token
        resp_login = self.http.post(url=host+path,
                             proxies=proxies,
                             headers=self.headers,
                             data=data_json
                             )
        assert resp_login.status_code==200
        resp_login_dict=json.loads(resp_login.text)
        return resp_login_dict