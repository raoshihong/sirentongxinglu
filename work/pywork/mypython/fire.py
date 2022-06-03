# python中的类

class Person:
    empCount = 0  # 类属性,所有实例共享,通过类名调用
    __secretCount = 0  # 私有属性

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.empCount += 1

    #  实例方法
    def run(self):
        print(self.name, self.age)

# 创建实例
p = Person("zhangsan",10)
# 调用方法
p.run()


# 类的继承
class Student(Person):
    __card = ""
    def __init__(self, card):
        self.__card = card

    def run(self):
        print(self.name, self.age, self.__card)

stu = Student("aaaa")
stu.name = "lisi"
stu.age = 20
stu.run()