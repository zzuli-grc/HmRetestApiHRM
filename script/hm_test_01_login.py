# 登录接口测试用例
import unittest

import sys

from api.login_api import LoginApi
import app
import logging
import utils
from parameterized import parameterized

from data.read_login_data import read_login


class TestLogin(unittest.TestCase):
    """登录接口测试类"""

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(read_login())
    def test_01(self, mobile, password, http_code, success, code, message):
        """登录接口测试方法"""
        # 发送接口请求
        response = self.login_api.login_interface(mobile, password)
        # 获取返回数据
        json_data = response.json()
        # 打印返回数据
        logging.info("返回数据为:{}".format(json_data))
        # 断言   这部分可封装为方法
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, json_data.get("success"))  # 断言success值
        # self.assertEqual(10000, json_data.get("code"))  # 断言code
        # self.assertIn("操作成功", json_data.get("message"))  # 断言message
        try:
            utils.assert_fun(self, response, http_code, success, code, message)
        except Exception as e:
            # 如果出现问题,获取异常信息
            exc = sys.exc_info()
            # 日志输出异常信息
            logging.info("异常信息为:{}".format(exc[1]))

    def test_02(self):
        """登录接口多参测试方法"""
        # 发送接口请求
        response = self.login_api.login_interface_param(mobile="13800000002", password="123456", param="laile")
        # 获取返回数据
        logging.info("多参返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, True, 10000, "操作成功！")

    def test_03(self):
        """登录接口少参测试方法"""
        # 发送接口请求
        response = self.login_api.login_interface_param(mobile="13800000002")
        # 获取返回数据
        logging.info("少参返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, False, 20001, "用户名或密码错误")

    def test_04(self):
        """登录接口错误参数测试方法"""
        # 发送接口请求
        response = self.login_api.login_interface_param(mobile="13800000002", passwd="123456")
        # 获取返回数据
        logging.info("错误参数返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, False, 20001, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main()
