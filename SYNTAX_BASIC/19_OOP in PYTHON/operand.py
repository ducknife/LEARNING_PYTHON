

class car:
    def __init__(self, cost):
        self.__cost = cost
    def __eq__(self, other):
        return self.__cost == other.__cost
    def __str__(self): 
        return f'{self.__cost}'
    
car1 = car(1024)
car2 = car(1024)
if car1 == car2:
    print(True)
print(car1)


class sophuc:
    def __init__(self, thuc, ao):
        self.__thuc = thuc
        self.__ao = ao
    def __add__(self, other):
        thuc1 = self.__thuc + other.__thuc
        ao1 = self.__ao + other.__ao
        return sophuc(thuc1, ao1)
    
    def __str__ (self): #ham nay giup in dep hon
        return f'{self.__thuc} + {self.__ao}j'
    
a = sophuc(1, 3)
b = sophuc(2, 4)
c = a + b
print(a, b, c, sep='\n')