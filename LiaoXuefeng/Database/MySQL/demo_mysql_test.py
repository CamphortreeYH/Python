import mysql.connector

#连接数据库:
mydb = mysql.connector.connect(
    host='localhost',    #数据库主机地址
    user='root',         # 数据库用户名
    passwd='123456',     # 数据库密码
    database="runoob_db" #直接连接数据库，如果数据库不存在，会输出错误信息：
)

mycursor = mydb.cursor()

# #创建数据库使用 "CREATE DATABASE" 语句，创建一个名为 runoob_db 的数据库：
# mycursor.execute("CREATE DATABASE runoob_db")

# #使用 "SHOW DATABASES" 语句来查看数据库是否存在：
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

# #使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在，以下创建一个名为 sites 的数据表：
# mycursor.execute("CREATE TABLE SITES (name VARCHAR(255), url VARCHAR(255))")

# #使用 "SHOW TABLES" 语句来查看数据表是否已存在：
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# #创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 语句来创建一个主键，主键起始值为 1，逐步递增。
# #如果我们的表已经创建，我们需要使用 ALTER TABLE 来给表添加主键：
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#插入数据使用 "INSERT INTO" 语句：
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
#val = ("RUNOOB", "https://www.runoob.com")
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
#
# # mycursor.execute(sql, val)
# #批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
# mycursor.executemany(sql, val)

# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
#
# mydb.commit() #数据表内容有更新，必须使用到该语句
#
# # print(mycursor.rowcount, "记录插入成功。")
# #如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码：
# print("1 条记录已插入, ID:", mycursor.lastrowid)

# # 查询数据使用 SELECT 语句：
# mycursor.execute("SELECT * FROM sites")
#
# # # 也可以读取指定的字段数据：
# # mycursor.execute("SELECT name, url FROM sites")
#
# # myresult = mycursor.fetchall()  # fetchall() 获取所有记录
#
# # 如果我们只想读取一条数据，可以使用 fetchone() 方法：
# myresult = mycursor.fetchone()
# print(myresult)
#
# # for x in myresult:
# #     print(x)

# # 如果我们要读取指定条件的数据，可以使用 where 语句：
# sql = "SELECT * FROM sites WHERE name = 'RUNOOB'"

# # 也可以使用通配符 %：
# sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
# sql = "SELECT * FROM sites WHERE name = %s"
# na = ("RUNOOB",)
#
# mycursor.execute(sql, na)

# # 查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
# sql = "SELECT * FROM sites ORDER BY name"

# # 按 name 字段字母的降序排序：
# sql = "SELECT * FROM sites ORDER BY name DESC"
# mycursor.execute(sql)

# # 如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定
# mycursor.execute("SELECT * FROM sites LIMIT 3")

# 也可以指定起始位置，使用的关键字是 OFFSET：
# mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1") #0 为 第一条，1 为第二条，以此类推
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

# # 删除记录使用 "DELETE FROM" 语句：
# sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录删除")

# 数据表更新使用 "UPDATE" 语句：
# sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, " 条记录被修改")

# 删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除：
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)