# import pytest,requests,json
# http = requests.session()
# proxies = {'http': 'http://localhost:8888'}
# # token=''
# # headers={}
#
# @pytest.fixture(scope='session', autouse=True)
# def session_fixture_login():
#     headers = {}
#     headers['Content-Type'] = 'application/json;charset=UTF-8'
#
#     resp = http.post(url="http://192.168.1.203:8083/sys/login",
#                          proxies=proxies,
#                          headers=headers,
#                          data='{"userName":"18210034706","password":"123456"}')
#     resp_dict = json.loads(resp.text)  # json转换成python的dict对象
#     token = resp_dict['object']['token']
#     headers['token'] = token
#     print('http code：%s' % resp.status_code)
#     assert resp.status_code==200
#     print("登录成功。。。。。")
#     yield
#     resp_out = http.post(url="http://192.168.1.203:8083/sys/logout",
#                      proxies=proxies,
#                      headers=headers
#                          )
#     print('http code：%s' % resp_out.status_code)
#     assert resp_out.status_code == 200
#     print("-----退出登录")

import pytest,requests,json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()

@pytest.fixture(scope='session', autouse=True)
def session_fixture_login():
    path='/sys/login'
    data={'userName':CommonData.mobile,'password':CommonData.password}
    resp_login=http.post(path,data)
    CommonData.token = resp_login['object']['token']
    code=resp_login['code']
    assert code==200
    print("登录成功。。。。。")
    yield
    path_out='/sys/logout'
    data_out=None
    resp_out = http.post(path_out,data_out)
    assert resp_out['code'] == 200
    print("-----退出登录")

