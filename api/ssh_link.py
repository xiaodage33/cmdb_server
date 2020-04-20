import  paramiko
import requests

def ssh_link(hostname,cmd):
    ssh=paramiko.SSHClient()  #创建链接对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许链接不在know——hosts文件中的主机

    ssh.connect(hostname=hostname,port=22,username='root',password='1234567') #链接服务器

    stdin,stdout,stderr=ssh.exec_command(cmd) #执行命令
    result =stdout.read()    #获取结果
    ssh.close()
    print(result.decode())
    return result.decode('utf-8')

def run():
    info = ssh_link('172.20.10.10','hostname')

    print('获取资产信息：',info)
    # result = requests.post(url='http://127.0.0.1:8888/cmdb/api',data={'host':'172.20.10.10','info':info})
    result = requests.post(url='http://127.0.0.1:8888/cmdb/api',json={'host':'172.20.10.10','info':info})


    print("把资产信息发送到api",result.text)





run()



