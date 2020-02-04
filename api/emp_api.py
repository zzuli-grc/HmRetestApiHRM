# 员工管理接口api
import app
import requests


class EmpApi(object):
    """员工管理接口类"""

    def __init__(self):
        self.url = app.HOST + "/api/sys/user"
        self.headers = app.HEADERS

    def emp_add_interface(self, username, mobile, work_num):
        """添加员工接口"""
        url = self.url
        # 添加员工数据
        data = {"username": username, "mobile": mobile, "workNumber": work_num}
        # 发送接口请求
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def emp_find_interface(self):
        """查询员工接口"""
        url = self.url + "/" + app.ID
        # 查询员工信息
        response = requests.get(url, headers=self.headers)
        return response

    def emp_update_interface(self, username):
        """修改员工接口"""
        url = self.url + "/" + app.ID
        data = {"username": username}
        # 发送接口请求
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def emp_del_interface(self):
        """删除员工接口"""
        url = self.url + "/" + app.ID
        response = requests.delete(url, headers=self.headers)
        return response
