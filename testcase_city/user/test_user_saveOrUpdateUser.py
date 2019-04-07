# import pytest
# from common.commonData import CommonData
# from conftest import http
# class Test_saveOrUpdateUser():
#     @pytest.mark.test
#     def test_user_saveOrUpdateUser(self):
#         path = '/user/saveOrUpdateUser'
#         data = {
#             "nickName": "小巫婆",
#             "userName": "13233377888",
#             "telNo": "",
#             "email": "",
#             "address": "",
#             "roles":""
#         }
#         resp_addUser = http.post(path, data)
#         assert resp_addUser['code']==200
#         # assert resp_addUser['msg']=='内部服务器异常，请联系研发人员'
#         print('新增用户成功')