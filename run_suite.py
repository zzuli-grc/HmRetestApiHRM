# 测试套件，执行用例
import unittest

from script.hm_test_02_emp import TestEmp
from tools.HTMLTestRunner import HTMLTestRunner

# 初始化测试套件
import app
from script.hm_test_01_login import TestLogin

suite = unittest.TestSuite()
# 组装登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
# 组装员工管理接口测试用例
suite.addTest(unittest.makeSuite(TestEmp))
# 测试报告路径
report_dir = app.BASE_DIR + "/report/iHRM.html"
# 运行测试用例并生成报告
with open(report_dir, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=1, title="iHRM人力资源管理系统接口测试", description="语言:Python,版本:v1.1")
    runner.run(suite)
