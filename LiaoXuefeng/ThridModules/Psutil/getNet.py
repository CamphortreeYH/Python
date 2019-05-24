import psutil

#psutil可以获取网络接口和网络连接信息：
print(psutil.net_io_counters())#获取网络读写字节/包的个数
print(psutil.net_if_addrs())#获取网络接口信息
print(psutil.net_if_stats())#获取网络接口状态

#要获取当前网络连接信息，使用net_connections()：
print(psutil.net_connections())