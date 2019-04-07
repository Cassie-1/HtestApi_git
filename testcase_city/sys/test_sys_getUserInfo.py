import pytest
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('展示用户信息模块')
class Test_getUserInfo():
    # @pytest.mark.test
    @allure.story('获取用户信息成功')
    def test_sys_getUserInfo(self):
        path = '/sys/getUserInfo'
        data = {
            'token': CommonData.token
        }
        resp_getUserInfo = http.post(path, data)
        assert resp_getUserInfo['code']==200
        assert resp_getUserInfo['msg']=='操作成功'
        print('获取用户信息成功')

    # @pytest.mark.test
    # def test_sys_getUserInfo_fail(self):
    #     path = '/sys/getUserInfo'
    #     data = {
    #         'token': 'asdfghjkl'
    #     }
    #     resp_getUserInfo = http.post(path, data)
    #     assert resp_getUserInfo['code']==200
    #     assert resp_getUserInfo['msg']=='操作成功'
    #     print('获取用户信息失败')