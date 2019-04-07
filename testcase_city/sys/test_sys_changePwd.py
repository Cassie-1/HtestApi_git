import pytest
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature('修改密码模块')
class Test_changePwd():
    @pytest.mark.test
    @allure.story('密码修改成功')
    def test_sys_changePwd(self):
        path = '/sys/changePwd'
        data = {
            'userId':97,
            'userName':CommonData.mobile,
            'oldPwd':CommonData.password,
            'password':'111111'
        }
        resp_changePwd = http.post(path, data)
        assert resp_changePwd['code']==200
        assert resp_changePwd['msg']=='操作成功'
        print('密码修改成功')
        self.reset_pwd()
    def reset_pwd(self):
        path = '/sys/changePwd'
        data = {
            'userId': 97,
            'userName': CommonData.mobile,
            'oldPwd': '111111',
            'password': '123456'
        }
        resp_changePwd = http.post(path, data)
        print('修改回原始密码')

    @pytest.mark.test
    @allure.story('旧密码错误')
    def test_sys_changePwd_error_oldpwd(self):
        path = '/sys/changePwd'
        data = {
            'userId': 97,
            'userName': CommonData.mobile,
            'oldPwd': '111111',
            'password': '111111'
        }
        resp_changePwd = http.post(path, data)
        assert resp_changePwd['code'] == 411
        assert resp_changePwd['msg'] == '旧密码错误'
        print('旧密码错误')