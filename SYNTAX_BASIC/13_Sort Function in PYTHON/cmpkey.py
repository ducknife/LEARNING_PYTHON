from functools import cmp_to_key

""" -1: tang dan, 1: giam dan, 0: bang """

def sumdigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum     

def cmp(a, b): #sap xep theo tong chu so giam dan
    if sumdigit(a) < sumdigit(b):
        return 1
    elif sumdigit(a) > sumdigit(b):
        return -1 #mong muon thi tra ve -1, nguoc lai thi la 1, con lai la 0
    else:
        return 0   


a = [1, 23, 211933, 1291, 331, 123]
a.sort(key = cmp_to_key(cmp))
print(a)

