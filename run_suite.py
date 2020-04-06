#导包
from tools.HTMLTestRunner_PY3 import HTMLTestRunner
from script.testEmp import testEmp
from script.testEmp2 import testEmp2
from script.testEmp3 import testEmp3
from script.testLogin import testLogin
from script.testLogin_params import testLoginParams
import unittest
import app,time,logging
#创建测试套件
suite = unittest.TestSuite()
#添加测试用例
suite.addTest(unittest.makeSuite(testEmp))
suite.addTest(unittest.makeSuite(testEmp2))
suite.addTest(unittest.makeSuite(testEmp3))
suite.addTest(unittest.makeSuite(testLogin))
suite.addTest(unittest.makeSuite(testLoginParams))
#指定测试报告路径
#report_file = app.BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_file = app.BASE_DIR + "/report/report.html"
logging.info("自动构建")
#生成测试报告
with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title="iHRM系统测试报告")
    runner.run(suite)