import pymysql

db = pymysql.connect(host='192.168.2.104', port=3306, password='mysql',
                     database='mytestdb', user='root', charset='utf8mb4')

cursor = db.cursor()
# sql = "INSERT INTO employee (name, age, sex, income) VALUES ('王五',24,'F',5000)"
sql = ("insert into employee (name, age, sex, income) values ('%s', '%s', '%s', '%s')") % ("张三2", 21, 'F', 3000)

try:
    cursor.execute(sql)
    db.commit()
    print("exec successfully")
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()
