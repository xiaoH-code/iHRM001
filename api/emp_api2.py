#创建员工的类，并封装员工相关的接口
import requests

class empApi():
    def __init__(self):
        self.adduser_url = "http://ihrm-test.itheima.net/api/sys/user"

    #添加员工
    def add_emp(self,session,name,mobile):
        adduser_data = {"username": name,
                        "mobile": mobile,
                        "timeOfEntry": "2019-07-01",
                        "formOfEmployment": 1,
                        "workNumber": "1322131",
                        "departmentName": "测试部",
                        "departmentId": "1066240656856453120",
                        "correctionTime": "2019-04-05"}
        add_resp = session.post(self.adduser_url,json=adduser_data)
        return add_resp

    #查询员工
    def query_emp(self,session,userid):
        emp_url = self.adduser_url + '/' + userid
        query_resp = session.get(emp_url)
        return query_resp

    #修改员工
    def modify_emp(self,session,userid,data):
        emp_url = self.adduser_url + '/' + userid
        modify_resp = session.put(emp_url,json=data)
        return modify_resp

    #删除员工
    def delete_emp(self,session,userid):
        emp_url = self.adduser_url + '/' + userid
        delete_resp = session.delete(emp_url)
        return delete_resp