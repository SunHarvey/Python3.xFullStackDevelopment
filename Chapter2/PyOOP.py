class People:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print('{0} 的性别是{1}'.format(self.name, self.gender))


class Student(People):
    def __init__(self, name, gender, grade):
        # super(Student, self).__init__(name, gender)
        People.__init__(self, name, gender)
        self.grade = grade

    def info(self):
        print('{0}说: 我的性别是{1},在读{2}年级'.format(self.name, self.gender, self.grade))

    def __call__(self, a):
        return a + 5


stu = Student("Tom", "mail", 3)
stu.speak()
stu.info()
print(stu(5))
