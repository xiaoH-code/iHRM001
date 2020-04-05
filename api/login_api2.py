#导包
import requests

#生成登录的api类
class loginApi():
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    # 封装登录接口
    def login(self,session,mobile,pwd):
        json_data = {"mobile":mobile, "password":pwd}
        response = session.post(self.login_url,json=json_data)
        return response