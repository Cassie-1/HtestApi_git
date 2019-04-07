# import pytest
# @pytest.fixture()
# def my_fixtures():
#     print("demo：我的初始化操作")
#     yield
#     print("*****demo数据恢复")
#
# class Test_demo:
#     @pytest.mark.usefixtures("my_fixtures")
#     @pytest.mark.debug
#     def test_first(this):
#         # assert 1==2
#         print('demo：我的第一个测试用例')
#         assert 1 != 2
#
#     @pytest.mark.usefixtures("my_fixtures")
#     def test_second(this):
#         print('demo：我的第二个测试用例')
#         assert 2 == 2
#
#     @pytest.mark.usefixtures("my_fixtures")
#     def test_third(this):
#         print('demo：我的第三个测试用例')
#         assert 'a' in 'ab'
#
#     @pytest.mark.usefixtures("my_fixtures")
#     def test_fourth(this):
#         print('demo：我的第四个测试用例')
#         b = [1, 2, 3]
#         assert 5 not in b