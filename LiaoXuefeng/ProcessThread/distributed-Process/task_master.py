# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务队列:
task_queue = queue.Queue()
#接受结果队列：
result_queue = queue.Queue()

#从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上， callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda : task_queue)
QueueManager.register('get_result', callable=lambda : result_queue)
#绑定端口5000，设置验证码'abc':
