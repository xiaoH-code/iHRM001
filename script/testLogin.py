#导包
import requests,unittest
from api.login_api import loginApi
from utils import assert_common_utils
#新建登录测试类，继承unittest.case类
class testLogin(unittest.TestCase):
    #初始化setup和teardown
    def setUp(self) -> None:
        self.login_api = loginApi()
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def tearDown(self) -> None:
        pass

    #创建登录的测试函数
    #登录成功
    def test01_login_success(self):
        response = self.login_api.login("13800000002",'123456')
        assert_common_utils(self,response,200,True,10000,'操作成功')

    #用户名不存在
    def test02_login_userNotExist(self):
        response = self.login_api.login("13888889999",'123456')
        assert_common_utils(self, response, 200, False, 20001, '用户名或密码错误')

    #密码错误
    def test03_login_WrongPassword(self):
        response = self.login_api.login("13800000002",'error')
        assert_common_utils(self, response, 200, False, 20001, '用户名或密码错误')

    #请求参数为空
    def test04_login_params_is_empty(self):
        response = requests.post(self.login_url)
        assert_common_utils(self, response, 200, False, 99999, '抱歉，系统繁忙，请稍后重试')

    #用户名为空
    def test05_login_username_is_null(self):
        response = self.login_api.login("",'123456')
        assert_common_utils(self, response, 200, False, 20001, '用户名或密码错误')

    #密码为空
    def test06_login_password_is_null(self):
        response = self.login_api.login("13800000002",'')
        assert_common_utils(self, response, 200, False, 20001, '用户名或密码错误')