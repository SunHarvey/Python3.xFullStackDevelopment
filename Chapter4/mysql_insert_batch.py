import pymysql

db = pymysql.connect(host='192.168.2.104', user='root', passwd='mysql', db='mytestdb',
                     charset='utf8mb4')
cursor = db.cursor()
sql = "insert into employee (name, age, sex, income) values (%s, %s,%s, %s)"
ls = []
employ1 = ("张三3", 22, "F", 4500)
employ2 = ("李四", 28, "M", 4500)

ls.append(employ1)
ls.append(employ2)

try:
    cursor.executemany(sql, ls)
    db.commit()
    print("exec successful")
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()
