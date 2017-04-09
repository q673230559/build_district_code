__author__ = 'Administrator'

'''
pip install PyMySQL
先要建立数据库   district_code
'''

import pymysql


def t():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='deepter123', db='district_code',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
        district_code(code INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, province VARCHAR(40),country VARCHAR(40),area VARCHAR(40))")
    cur.execute("INSERT INTO district_code (code,province,country,area) VALUES(1,'河南','中国','省')".encode("utf-8"))
    # 提交，保存新建或修改的数据
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()


t()


def c():
    # 创建链接对象
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='deepter123', db='goods')
    # 创建游标s
    cursor = conn.cursor()
    # 执行sql，更新单条数据，并返回受影响行数
    # effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
    # 插入多条，并返回受影响的函数
    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)",[("1.0.0.1",1,),("10.0.0.3",2)])
    # 获取最新自增ID
    # new_id = cursor.lastrowid
    # 查询数据
    cursor.execute("select * from t_user")
    # 获取一行
    row_1 = cursor.fetchone()
    # 获取多(3)行
    row_2 = cursor.fetchmany(3)
    # 获取所有
    row_3 = cursor.fetchall()
    print(row_3)
    # 重设游标类型为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 提交，保存新建或修改的数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()