import pymysql

db = pymysql.connect(host='192.168.2.104', user='root', passwd='mysql', db='mytestdb',
                     charset='utf8mb4')
cursor = db.cursor()

sql = "update employee set `age` = '%d' where `id`='%s' " % (28, 1)
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()
