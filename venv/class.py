class Student:
    '所有学生的基类name,age'
    stuCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stuCount += 1

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

    def __str__(self):
        print("Name : ", self.name, ", age: ", self.age)

    def displayCount(self):
        print("Total:",Student.stuCount)

s1=Student("aaa",11)
s1.__str__()
s1.displayCount()

s2=Student("bbb",12)
s2.__str__()
s2.displayCount()

s3=s2
s3.age=13
s2.__str__()
del s1
del s2#无法销毁
s3.__str__()
print(111)
#second commit
#push commit