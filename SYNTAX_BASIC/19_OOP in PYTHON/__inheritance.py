class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def on_screen(self):
        return f'{self.name} {self.age}'

class child(parent):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        #parent.__init(self, name, age)
        self.gpa = gpa
    def on_screen(self):
        return super().on_screen() + f' {self.gpa:.2f}'
        #parent.on_screen(self) + f' {self.gpa:.2f}'

child2 = parent("Cuong", "1978")

child1 = child('Hung', 20, 4.0000)
print(child1.on_screen())