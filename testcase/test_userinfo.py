# import pytest
# @pytest.fixture()
# def my_fixtures():
#     print("用户信息管理：我的初始化操作")
#     yield
#     print("-*-*-*用户管理模块：数据恢复")
# @pytest.mark.usefixtures("my_fixtures")
# def test_first():
#     # assert 1==2
#     print('用户信息管理：我的第一个测试用例')
#     assert 1!=2
#
# @pytest.mark.usefixtures("my_fixtures")
# def test_second():
#     print('用户信息管理：我的第二个测试用例')
#     assert 2==2
#
# @pytest.mark.usefixtures("my_fixtures")
# @pytest.mark.debug
# def test_third():
#     print('用户信息管理：我的第三个测试用例')
#     assert 'a' in 'ab'
#
# @pytest.mark.usefixtures("my_fixtures")
# def test_fourth():
#     print('用户信息管理：我的第四个测试用例')
#     b=[1,2,3]
#     assert 5 not in b
#
# @pytest.mark.usefixtures("my_fixtures")
# def test_five():
#     print('用户信息管理：我的第五个测试用例')
#     assert assValue(5,3)
# def assValue(a,b):
#     if a>b :
#         return True
#     else:
#         return False
#
#
# # if __name__ == '__main__':
# #     pytest.main()