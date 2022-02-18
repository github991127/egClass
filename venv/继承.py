class Student:
    '所有学生的基类name,age'
    stuCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stuCount += 1

    def __del__(self):
        class_name = self
        print(class_name, "销毁")

    def displayCount(self):
        print("Total:",Student.stuCount)

    def displayStu(self):
        print("Name : ", self.name, ", age: ", self.age)

class Boy(Student):
    def __init__(self, name, age,sport):
        super(Boy, self).__init__(name, age)
        self.sport =  sport
    def displayStu(self):
        super(Boy, self).displayStu()
        print("sport:",self.sport)

b1=Boy('aaa',11,'soccer')
b1.displayStu()
b1.displayCount()