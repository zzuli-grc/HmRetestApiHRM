# 员工管理接口测试类
import logging
import unittest

import app
import utils
from api.emp_api import EmpApi
from api.login_api import LoginApi


class TestEmp(unittest.TestCase):
    """员工管理接口测试类"""

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_login(self):
        """登录接口"""
        # 发送接口请求
        response = self.login_api.login_interface(13800000002, 123456)
        # 获取token
        token = response.json().get("data")
        app.HEADERS["Authorization"] = "Bearer " + token
        logging.info("返回数据为:{}".format(response.json()))

    def test_02_emp_add(self):
        """添加员工"""
        # 发送接口请求
        response = self.emp_api.emp_add_interface("d121", "15978812348", "3")
        # 获取员工ID
        app.ID = response.json().get("data").get("id")
        # 打印返回数据
        logging.info("返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, True, 10000, "操作成功！")
        pass

    def test_03_emp_find(self):
        """查询员工"""
        # 发送接口请求
        response = self.emp_api.emp_find_interface()
        # 打印返回数据
        logging.info("返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, True, 10000, "操作成功！")

    def test_04_emp_update(self):
        """修改员工"""
        # 发送接口请求
        response = self.emp_api.emp_update_interface("小阿giao")
        # 打印返回数据
        logging.info("返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, True, 10000, "操作成功！")
        # 查询数据库
        with utils.DBUtil() as db_util:
            sql = "select username from bs_user where id={}".format(app.ID)
            db_util.execute(sql)
            text = db_util.fetchone()[0]
            logging.info("返回数据为:{}".format(text))
            try:
                self.assertIn('小阿giao', text)
            except AssertionError as e:
                raise e

    def test_05_emp_del(self):
        """删除员工"""
        # 发送接口请求
        response = self.emp_api.emp_del_interface()
        # 打印返回数据
        logging.info("返回数据为:{}".format(response.json()))
        # 断言
        utils.assert_fun(self, response, 200, True, 10000, "操作成功！")
        # 查询数据库
        with utils.DBUtil() as db_util:
            sql = "select username from bs_user where id={}".format(app.ID)
            db_util.execute(sql)
            text = db_util.fetchone()
            logging.info("返回数据为:{}".format(text))


if __name__ == '__main__':
    unittest.main()
