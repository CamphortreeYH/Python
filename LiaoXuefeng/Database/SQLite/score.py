# -*- coding: utf-8 -*-

import os, sqlite3

#os.path.join()函数用于路径拼接文件路径。
#os.path.dirname(__file__)返回脚本的路径, 如python c:/test/test.py 则返回路径 c:/test
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")

def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    cursor.execute('select name from user where score >= ? and score <= ? order by score', (low, high))
    values = cursor.fetchall()
    names = list(name[0] for name in values)
    return names

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95) #valures = [('Adam',)]
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80) #valures = [('Bart',), ('Lisa',)]
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100) #valures = [('Bart',), ('Lisa',), ('Adam',)]
print('Pass')

cursor.close()
conn.commit()
conn.close()