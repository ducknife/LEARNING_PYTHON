class person:
    def __init__ (self, name, age, job):
        self.name = name #public
        self._age = age #protected
        self.__job = job #private
    def infor(self): #lay thuoc tinh private or protected bang phuong thuc
        print(self.__job)
    def get_name(self):
        return f'xin chao {self.name}'
    def set_name(self, name):
        self.name = name


p1 = person("Hung", 20, "AI engineer")
p1.infor()
print(p1.get_name())
p1.set_name("empty")
print(p1.get_name())

