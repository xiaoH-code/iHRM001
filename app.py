#配置全局变量
import logging,os,time
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#初始化日志配置函数：
def init_log_config():
    # 1、创建日志器
    logger = logging.getLogger()
    #2、设置日志级别
    logger.setLevel(logging.INFO)
    #3、创建控制台处理器
    sh = logging.StreamHandler()
    #4、指定日志文件的路径，并创建日志文件处理器
    log_path = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,when='S',interval=5,backupCount=3,encoding='utf-8')
    #5、定义日志文件的格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)]  %(message)s'
    formatter = logging.Formatter(fmt)
    #6、将格式化器设置到控制台处理器和日志文件处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #7、将控制器处理器和日志文件处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)