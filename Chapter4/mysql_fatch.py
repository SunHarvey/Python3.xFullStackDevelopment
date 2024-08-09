import pymysql

db = pymysql.connect(host='192.168.2.104', user='root', passwd='mysql', db='mytestdb', charset='utf8mb4')
cursor = db.cursor()

sql = "select * from employee where `income` > '%d' " % (2000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print(id, name, age, sex, income)
except Exception as e:
    print(e)
finally:
    db.close()
