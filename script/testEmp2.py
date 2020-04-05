#导包
import logging
import unittest,requests
from api.login_api2 import loginApi
from api.emp_api2 import empApi
#新建员工测试类，继承unittest.TestCase类
from utils import assert_common_utils


class testEmp2(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = loginApi()
        self.emp_api = empApi()
        self.session = requests.Session()
        self.adduser_url = "http://ihrm-test.itheima.net/api/sys/user"

    def tearDown(self) -> None:
        self.session.close()

    # 创建员工的测试函数
    def test_emp_manage(self):
        #完成登录
        login_resp = self.login_api.login(self.session,'13800000002','123456')
        logging.info("login_resp={}".format(login_resp.json()))
        assert_common_utils(self, login_resp, 200, True, 10000, '操作成功')
        #登录成功后，获取cookie数据，并拼接为token
        b_token = "Bearer " + login_resp.json().get('data')
        logging.info("token={}".format(b_token))

        #添加员工
        add_resp = self.emp_api.add_emp(self.session,"tom","13012341118")
        logging.info("add_resp={}".format(add_resp.json()))
        assert_common_utils(self, add_resp, 200, True, 10000, '操作成功')

        #获取员工ID
        userid = add_resp.json().get('data').get('id')
        logging.info("userid={}".format(userid))
        #查询员工
        query_resp = self.emp_api.query_emp(self.session,userid)
        logging.info("query_resp={}".format(query_resp.json()))
        #断言
        assert_common_utils(self, query_resp, 200, True, 10000, '操作成功')

        #修改员工
        modify_data = {"username":"tom-new"}
        modify_resp = self.emp_api.modify_emp(self.session,userid,modify_data)
        logging.info("modify_resp={}".format(modify_resp.json()))
        # 断言
        assert_common_utils(self, modify_resp, 200, True, 10000, '操作成功')

        #删除员工
        delete_resp = self.emp_api.delete_emp(self.session,userid)
        logging.info("delete_resp={}".format(delete_resp.json()))
        # 断言
        assert_common_utils(self, delete_resp, 200, True, 10000, '操作成功')