# '''
# pip install PyMySQL
# 先要建立数据库   district_code
# doc里面第一行要出现不等于三个逗号
# '''

import pymysql

file = open("../doc/最新县及县以上行政区划代码（截止2016年7月31日）.txt", encoding='utf-8')

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='deepter123', db='district_code',
                       charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS \
        district_code(code INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, province VARCHAR(40),country VARCHAR(40),area VARCHAR(40))")

while 1:
    line = file.readline()
    if not line:
        break
    r = line.strip("\n").split(",")
    if len(r) == 4:
        print(r)
        sql_str = "INSERT INTO district_code (code,province,country,area) VALUES(" + r[0] + ",'" + r[1] + "','" + r[
            2] + "','" + r[3] + "')"
        cur.execute(sql_str.encode("utf-8"))
    pass


# 提交，保存新建或修改的数据
conn.commit()
# 关闭游标
cur.close()
# 关闭连接
conn.close()

