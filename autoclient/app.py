from plugins.disk import  DiskPlugin
from plugins.memory import MemoryPlugin
from plugins.network import NetWorkPlugin

# def run():  #不用这种方式
#     obj1 = DiskPlugin()
#     diskinfo = obj1.process()
#     obj2 = MemoryPlugin()
#     memory = obj2.process()
#     obj3 = NetWorkPlugin()
#     network = obj3.process()


#这种方式
import importlib

from settings import PLUGIN_CLASS_LIST

def run():
    for key,path in PLUGIN_CLASS_LIST.items():
        # print(key,path)  #key=disk    path=lib.plugins.disk.DiskPlugin ,
        #基于反射操作，先找到模块路径导入
        module_path,class_name = path.rsplit('.',maxsplit=1) #从右边往左第一个点
        module = importlib.import_module(module_path)  #根据字符串导入字符串

        #DiskPlugin这个可能也是变化的所以，要getattr
        cls = getattr(module,class_name)  #类就获取了
        plugins_object = cls()
        info = plugins_object.process()

        # print(key,cls()) #cls输出类名，（）实例化，

        print(key,info)

if __name__=='__main__':
    run()



# import  paramiko
# import requests
#
# def ssh_link(hostname,cmd):
#     ssh=paramiko.SSHClient()  #创建链接对象
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许链接不在know——hosts文件中的主机
#
#     ssh.connect(hostname=hostname,port=22,username='root',password='1234567') #链接服务器
#
#     stdin,stdout,stderr=ssh.exec_command(cmd) #执行命令
#     result =stdout.read()    #获取结果
#     ssh.close()
#     print(result.decode())
#     return result.decode('utf-8')
#
# def run():
#     info = ssh_link('172.20.10.10','hostname')
#
#     print('获取资产信息：',info)
#     # result = requests.post(url='http://127.0.0.1:8888/cmdb/api',data={'host':'172.20.10.10','info':info})
#     result = requests.post(url='http://127.0.0.1:8888/cmdb/api',json={'host':'172.20.10.10','info':info})
#
#
#     print("把资产信息发送到api",result.text)
#
#
#
#
#
# run()
#
#
#
