# import pytest
# from common.commonData import CommonData
# from conftest import http
# class Test_saveOrUpdateUser():
#     @pytest.mark.aaa
#     def test_saveOrUpdateUser(self):
#         data = {
#             'nickName': '16914785277',
#             'userName': '16914785277',
#             'telNo': '',
#             'email': '',
#             'address': '',
#             'roleIds': '',
#             'regionId': 1,
#             'regionLevel': 1
#         }
#         resp = http.post('/user/saveOrUpdateUser', data)
#         assert resp['code'] == 200
#         assert resp['msg'] == '操作成功'
#         print(resp['code'], resp['msg'], '注册成功')
#
#         # resp_addUser = http.post('/user/saveOrUpdateUser', data)
#         # assert resp_addUser['code']==200
#         # # assert resp_addUser['msg']=='内部服务器异常，请联系研发人员'
#         # print('新增用户成功')
#         # return resp_addUser['userName']
#
#     # @pytest.mark.test_user
#     # def test_user_saveOrUpdateUser1(self):
#     #     path = '/user/loadUserList'
#     #     data = {
#     #             "pageCurrent": 1,
#     #             "pageSize": 10,
#     #             "nickName": "",
#     #             "userName": "",
#     #             "regionId": 1
#     #     }
#     #     resp_addUser = http.post(path, data)
#     #     assert resp_addUser['code'] == 200
#     #     id=resp_addUser['object']['list'][0]['id']
#     #     # assert resp_addUser['msg']=='内部服务器异常，请联系研发人员'
#     #     print('得到新增用户的id')
#     #     # return resp_addUser['userName']
#     #
#     # @pytest.mark.test_user
#     # def test_user_UpdateUser(self):
#     #     path = '/user/saveOrUpdateUser'
#     #     data = {
#     #         "nickName": "16914785236",
#     #         "userName": "16914785236",
#     #         "telNo": "",
#     #         "email": "",
#     #         "address": "",
#     #         "roleIds": "1",
#     #         "regionId": 1,
#     #         "regionLevel": 1,
#     #         "id": self.test_user_saveOrUpdateUser1.id
#     #     }
#     #     resp_addUser = http.post(path, data)
#     #     assert resp_addUser['code'] == 200
#     #     id = resp_addUser['object']['list'][0]['id']
#     #     # assert resp_addUser['msg']=='内部服务器异常，请联系研发人员'
#     #     print('得到新增用户的id')
#     #
#     #
#     # @pytest.mark.test_user
#     # def test_login_success(self):
#     #     path = '/sys/login'
#     #     data = {
#     #         'userName': CommonData.mobile,
#     #         'password': CommonData.password
#     #     }
#     #     resp_login = http.post(path, data)
#     #     assert resp_login['code'] == 200
#     #     assert resp_login['msg'] == '操作成功'
#     #     id = resp_login['']
#     #     print('登录成功')
#     #
#     # @pytest.mark.test_user
#     # def test_login_success(self):
#     #     path = '/sys/login'
#     #     data = {
#     #         'userName': '13255577888',
#     #         'password': CommonData.password
#     #     }
#     #     resp_login = http.post(path, data)
#     #     assert resp_login['code']==200
#     #     assert resp_login['msg']=='操作成功'
#     #     id=resp_login['']
#     #     print('登录成功')
#
