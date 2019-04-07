# import pytest,requests
# from common.commonData import CommonData
# from conftest import http
#
# # @pytest.mark.test
# def test_getUserInfo():
#     path='/sys/getUserInfo'
#     data={'token':CommonData.token}
#     resp=http.post(path,data)
#     assert resp['code']==200
#     print('获取用户信息成功')