#导包
import logging
import unittest,requests
from api.login_api import loginApi
from api.emp_api import empApi
#新建员工测试类，继承unittest.TestCase类
from utils import assert_common_utils, get_data_adduser, get_data_query_user, get_data_modify_user, get_data_delete_user
from parameterized import parameterized
import app
import pymysql


class testEmp3(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = loginApi()
        self.emp_api = empApi()
        self.adduser_url = "http://ihrm-test.itheima.net/api/sys/user"

    def tearDown(self) -> None:
        pass

    # 创建员工的测试函数

    def test01_login(self):
        #完成登录
        login_resp = self.login_api.login('13800000002','123456')
        logging.info("login_resp={}".format(login_resp.json()))
        assert_common_utils(self, login_resp, 200, True, 10000, '操作成功')
        #登录成功后，获取cookie数据，并拼接为token
        b_token = "Bearer " + login_resp.json().get('data')
        logging.info("token={}".format(b_token))
        app.headers = {'Authorization':b_token,"Content-Type": "application/json"}

    @parameterized.expand(get_data_adduser)
    def test02_adduser(self,username,mobile,statusCode,success,code,msg):
        add_resp = self.emp_api.add_emp(username,mobile,app.headers)
        logging.info("add_resp={}".format(add_resp.json()))
        assert_common_utils(self, add_resp, statusCode, success, code, msg)

        #获取员工ID
        app.userid = add_resp.json().get('data').get('id')
        logging.info("userid={}".format(app.userid))

    @parameterized.expand(get_data_query_user)
    def test03_query(self,statusCode,success,code,msg):
        #查询员工
        query_resp = self.emp_api.query_emp(app.userid,app.headers)
        logging.info("query_resp={}".format(query_resp.json()))
        #断言
        assert_common_utils(self, query_resp, statusCode, success, code, msg)

    @parameterized.expand(get_data_modify_user)
    def test04_modify(self,newname,statusCode,success,code,msg):
        #修改员工
        modify_data = {"username":newname}
        modify_resp = self.emp_api.modify_emp(app.userid,modify_data,app.headers)
        logging.info("modify_resp={}".format(modify_resp.json()))
        # 断言
        assert_common_utils(self, modify_resp, statusCode, success, code, msg)

        # #导包
        # #建立连接
        # conn = pymysql.connect('182.92.81.159','readuser','iHRM_user_2019','ihrm')
        # #创建游标
        # cursor = conn.cursor()
        # #执行sql
        # sql = "select username from bs_user where id = %s"
        # cursor.execute(sql,app.userid)
        # name = cursor.fetchone()[0]
        # #关闭游标
        # cursor.close()
        # #关闭连接
        # conn.close()
        # self.assertEqual("tom-new", name)

    @parameterized.expand(get_data_delete_user)
    def test05_delete(self,statusCode,success,code,msg):
        #删除员工
        delete_resp = self.emp_api.delete_emp(app.userid,app.headers)
        logging.info("delete_resp={}".format(delete_resp.json()))
        # 断言
        assert_common_utils(self, delete_resp, statusCode, success, code, msg)