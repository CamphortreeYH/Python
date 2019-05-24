import psutil

#通过psutil可以获取到所有进程的详细信息：
print(psutil.pids()) #所有进程ID

p = psutil.Process(3816) #获取指定进程ID=3816
print(p.name) #进程名称
print(p.exe) #进程exe路径
print(p.cwd) #进程工作目录
print(p.cmdline()) # 进程启动的命令行
print(p.ppid) # 父进程ID
print(p.children()) # 子进程列表
print(p.status()) # 进程状态
print(p.username()) # 进程状态
print(p.create_time()) # 进程创建时间
print(p.terminal()) # 进程终端
print(p.cpu_times) # 进程使用的CPU时间
print(p.memory_info) # 进程使用的内存
print(p.open_files()) # 进程打开的文件
print(p.connections()) # 进程相关网络连接
print(p.nunum_threads()) # 进程的线程数量
print(p.threads()) # 所有线程信息
print(p.terminate) # 结束进程
