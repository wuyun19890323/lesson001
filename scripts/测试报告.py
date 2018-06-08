import time
from HTMLTestRunner import HTMLTestRunner
import unittest

# 加载当前目录下iweb开头的.py文件
discover = unittest.defaultTestLoader.discover("./", pattern="test*.py")
if __name__ == '__main__':
    file_dir = "../Report/"
    # 定义报告名称格式
    nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告完整路径和名称
    file_name = file_dir + nowtime + "Report.html"
    with open(file_name, "wb")as f:
        # 实例化HTMLTestRunner对象，传入报告文件流f
        runner = HTMLTestRunner(stream=f, title="iweb_shop项目Web自动化测试报告", description="测试用例共计9条")
        runner.run(discover)
