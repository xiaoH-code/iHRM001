#导包
import logging,pymysql
import unittest,requests
from api.login_api import loginApi
from api.emp_api import empApi
#新建员工测试类，继承unittest.TestCase类
from utils import assert_common_utils
from utils import DButils


class testEmp(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = loginApi()
        self.emp_api = empApi()
        self.dbutils = DButils()
        self.adduser_url = "http://ihrm-test.itheima.net/api/sys/user"

    def tearDown(self) -> None:
        pass

    # 创建员工的测试函数
    def test_emp_manage(self):
        #完成登录
        login_resp = self.login_api.login('13800000002','123456')
        logging.info("login_resp={}".format(login_resp.json()))
        assert_common_utils(self, login_resp, 200, True, 10000, '操作成功')
        #登录成功后，获取cookie数据，并拼接为token
        b_token = "Bearer " + login_resp.json().get('data')
        logging.info("token={}".format(b_token))

        #添加员工
        headers = {'Authorization':b_token,"Content-Type": "application/json"}
        add_resp = self.emp_api.add_emp("tom","13012341119",headers)
        logging.info("add_resp={}".format(add_resp.json()))
        assert_common_utils(self, add_resp, 200, True, 10000, '操作成功')

        #获取员工ID
        userid = add_resp.json().get('data').get('id')
        logging.info("userid={}".format(userid))
        #查询员工
        query_resp = self.emp_api.query_emp(userid,headers)
        logging.info("query_resp={}".format(query_resp.json()))
        #断言
        assert_common_utils(self, query_resp, 200, True, 10000, '操作成功')

        #修改员工
        modify_data = {"username":"tom-new"}
        modify_resp = self.emp_api.modify_emp(userid,modify_data,headers)
        logging.info("modify_resp={}".format(modify_resp.json()))
        # 断言
        assert_common_utils(self, modify_resp, 200, True, 10000, '操作成功')

        #执行sql
        # sql = "select username from bs_user where id = {}".format(userid)
        # data = self.dbutils.cls_getone(sql)
        # self.assertEqual("tom-new", data[0])

        #删除员工
        delete_resp = self.emp_api.delete_emp(userid,headers)
        logging.info("delete_resp={}".format(delete_resp.json()))
        # 断言
        assert_common_utils(self, delete_resp, 200, True, 10000, '操作成功')