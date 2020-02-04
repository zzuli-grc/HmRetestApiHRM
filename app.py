# 初始化日志文件
import logging
import os
from logging import handlers

# 设置文件的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 接口地址
HOST = "http://182.92.81.159"
# 请求头
HEADERS = {"Content-Type": "application/json"}
ID = None


def init_logging():
    """初始化日志函数"""
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器(控制台处理器,文件处理器)
    # 设置控制台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    file_name = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(file_name, when="M", interval=1, backupCount=7)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formartter = logging.Formatter(fmt)
    # 将格式化器添加到处理器
    sh.setFormatter(formartter)
    fh.setFormatter(formartter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
