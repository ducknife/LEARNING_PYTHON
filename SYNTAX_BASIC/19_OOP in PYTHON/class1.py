class Person:
    pass #tao class rỗng

p = Person()
print(type(p))  

class Dog:
    sex = "female" #thuộc tính chung
    def __init__(self, name, job): #chứa các thuộc tính riêng
        self.name = name
        self.job = job
    def infor(self):
        print(self.name + " " + self.job)
    def inputfromkb(self):
        self.name = input()
        self.job = input()


dog1 = Dog("skibidi", "pet")
dog2 = Dog("skubidu", "pet")
print(dog1.sex, dog2.sex)
dog1.infor()
dog3 = Dog("", "")
dog3.inputfromkb()
dog3.infor()