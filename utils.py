import pymysql,json,app
#封装公共的校验方法
def assert_common_utils(self,response,statuscode,success,code,msg):
    self.assertEqual(statuscode, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(msg, response.json().get('message'))

def read_data_login():
    data_file = app.BASE_DIR + "/data/login.json"
    with open(data_file,'r',encoding='utf-8') as f:
        #读取json数据文件
        json_data = json.load(f)
        #依次读取json数据文件中的数据，并保存为list
        #{"desc":"登录成功","username": "13800000002","password": "123456","statusCode": "200","success": "True","code": "10000","msg": "操作成功"}
        case_list = []
        for data in json_data:
            username = data.get('username')
            password = data.get('password')
            statusCode = data.get('statusCode')
            success = data.get('success')
            code = data.get('code')
            msg = data.get('msg')
            case_list.append((username,password,statusCode,success,code,msg))
    print("读取出来的数据为：{}".format(case_list))
    return case_list

def get_data_adduser():
    data_file = app.BASE_DIR + "/data/employee.json"
    with open(data_file,'r',encoding='utf-8') as f:
        json_data = json.load(f)
        caselist = []
        add_data = json_data.get('add_user')
        username = add_data.get('username')
        mobile = add_data.get('mobile')
        statusCode = add_data.get('statusCode')
        success = add_data.get('success')
        code = add_data.get('code')
        msg = add_data.get('msg')
        caselist.append((username,mobile,statusCode,success,code,msg))
    return caselist

def get_data_query_user():
    data_file = app.BASE_DIR + "/data/employee.json"
    with open(data_file,'r',encoding='utf-8') as f:
        json_data = json.load(f)
        caselist = []
        add_data = json_data.get('query_user')
        statusCode = add_data.get('statusCode')
        success = add_data.get('success')
        code = add_data.get('code')
        msg = add_data.get('msg')
        caselist.append((statusCode,success,code,msg))
    return caselist

def get_data_modify_user():
    data_file = app.BASE_DIR + "/data/employee.json"
    with open(data_file,'r',encoding='utf-8') as f:
        json_data = json.load(f)
        caselist = []
        add_data = json_data.get('modify_user')
        newname = add_data.get('newname')
        statusCode = add_data.get('statusCode')
        success = add_data.get('success')
        code = add_data.get('code')
        msg = add_data.get('msg')
        caselist.append((newname,statusCode,success,code,msg))
    return caselist

def get_data_delete_user():
    data_file = app.BASE_DIR + "/data/employee.json"
    with open(data_file,'r',encoding='utf-8') as f:
        json_data = json.load(f)
        caselist = []
        add_data = json_data.get('delete_user')
        statusCode = add_data.get('statusCode')
        success = add_data.get('success')
        code = add_data.get('code')
        msg = add_data.get('msg')
        caselist.append((statusCode,success,code,msg))
    return caselist

class DButils:
    conn,cursor = None,None

    @classmethod
    def cls_setup(cls):
        #建立连接
        cls.conn = pymysql.connect('182.92.81.159','readuser','iHRM_user_2019','ihrm')
        #创建游标
        cls.cursor = cls.conn.cursor()
        return cls.cursor

    @classmethod
    def cls_teardown(cls):
        if cls.cursor:
            cls.cursor.close()
        if cls.conn:
            cls.conn.close()

    @classmethod
    def cls_getone(cls,sql):
        try:
            cursor = cls.cls_setup()
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as e:
            print("Exception is ",e)
        finally:
            cls.cls_teardown()
        return data

