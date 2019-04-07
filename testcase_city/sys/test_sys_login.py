import pytest
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('登录模块')
class Test_login():

    # @pytest.mark.test
    @allure.story('登录成功')
    def test_login_success(self):
        path = '/sys/login'
        data = {
            'userName': CommonData.mobile,
            'password': CommonData.password
        }
        resp_login = http.post(path, data)
        assert resp_login['code']==200
        assert resp_login['msg']=='操作成功'
        assert resp_login['object']['userId']==97
        print('登录成功')

    # @pytest.mark.test
    @allure.story('用户名或密码错误')
    def test_login_fail_error_pwd(self):
        path = '/sys/login'
        data = {
            'userName': CommonData.mobile,
            'password': '111111'
        }
        resp_login = http.post(path, data)
        assert resp_login['code']==410
        assert resp_login['msg']=='用户名或密码错误'
        print('用户名或密码错误')


    # @pytest.mark.test
    @allure.story('用户不存在')
    def test_login_fail_error_user(self):
        path = '/sys/login'
        data = {
            'userName': '12345678912',
            'password': CommonData.password
        }
        resp_login = http.post(path, data)
        assert resp_login['code']==301
        assert resp_login['msg']=='用户不存在'
        print('用户不存在')

    # @pytest.mark.test
    @allure.story('用户不存在')
    def test_login_fail_error_user_none(self):
        path = '/sys/login'
        data = {
            'userName': None,
            'password': CommonData.password
        }
        resp_login = http.post(path, data)
        assert resp_login['code']==301
        assert resp_login['msg']=='用户不存在'
        print('用户不存在')