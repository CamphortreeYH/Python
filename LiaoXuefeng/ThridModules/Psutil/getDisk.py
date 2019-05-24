import psutil

#可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions())#磁盘分区信息
print(psutil.disk_usage('/'))#磁盘使用情况
print(psutil.disk_io_counters())#磁盘IO