# 登录接口api
import requests
import app


class LoginApi(object):
    """登录接口类"""

    def __init__(self):
        """获取登录接口url"""
        self.url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login_interface(self, mobile, password):
        """登录接口"""
        # 获取json数据
        data = {"mobile": mobile, "password": password}
        # 发送接口请求
        response = requests.post(self.url, headers=self.headers, json=data)
        return response

    def login_interface_param(self, **kwargs):
        """登录接口参数"""
        # 获取json数据
        data = {}
        if kwargs:
            for k, v in kwargs.items():
                data[k] = v
            print(data)
        # 发送接口请求
        response = requests.post(self.url, json=data, headers=self.headers)
        return response
