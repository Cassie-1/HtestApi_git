from common.commonData import CommonData
from conftest import http
import random,pytest
import allure

@allure.feature('用户信息模块')
class Test_User():
    @allure.story('添加新用户查看')
    def test_saveOrUpdateUser(this):
        nickname = str(random.randint(10000000, 100000000))
        mobile = '159' + nickname
        data={
            'nickName':nickname,
            'userName':mobile,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "",
            "regionId": 1,
            "regionLevel": 1
        }
        resp=http.post('/user/saveOrUpdateUser',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print(resp['code'],resp['msg'],'注册成功')
        # 新用户登录
        login_data={
            'userName':mobile,
            'password':CommonData.password
        }
        resp_new_login=http.post('/sys/login',login_data)
        assert resp_new_login['code'] == 200
        assert resp_new_login['msg'] == '操作成功'
        print(resp_new_login['code'],resp_new_login['msg'],'新用户登录成功')
        id=resp_new_login['object']['userId']
        print(id)
        # 获取用户列表
        user_data={
            "pageCurrent": 1,
            "pageSize": 10,
            "nickName": "",
            "userName": "",
            "regionId": 1
        }
        resp_user_list=http.post('/user/loadUserList',user_data)
        assert resp_user_list['code'] == 200
        assert resp_user_list['msg'] == '操作成功'
        user_id=resp_user_list['object']['list'][0]['id']
        assert id==user_id
        print('用户id一样')
        # 查看用户详细信息
        user_info_data={
            "id": id
        }
        resp_user_list = http.post('/user/loadUserList', user_info_data)
        assert resp_user_list['code'] == 200
        assert resp_user_list['msg'] == '操作成功'

