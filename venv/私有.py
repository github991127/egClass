class A:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print('secret',self.__secretCount)

counter = A('aaa',2)
counter.count()
counter.count()
print('public',counter.publicCount)
#print('secret',counter.__secretCount)  # 报错，实例不能访问私有变量
print('public',counter.name)