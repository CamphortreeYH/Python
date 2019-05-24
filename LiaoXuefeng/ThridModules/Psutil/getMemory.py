import psutil

#使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())