# import traceback
#
# try:
#     print(1/0)
# except:
#     traceback.print_exc()
# else:
#     print("elsee")
# finally:
#     print("finalyyy")

class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    a = 6
    b = 4

    if a > b:
        raise MyException("自定义异常")
except MyException as e1:
    print("打印MyException异常", e1)

except Exception as e:
    print("打印Exception异常", e)
