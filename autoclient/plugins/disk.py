#采集硬盘数据

class DiskPlugin(object):
    def process(self):
        #假设执行命令后返回信息
        return  {'disk':'300g'}