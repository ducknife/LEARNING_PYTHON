from functools import cmp_to_key

class monhoc:
    def __init__(self, ma_mon, ten_mon, hinh_thuc):
        self.__ma_mon = ma_mon
        self.__ten_mon = ten_mon
        self.__hinh_thuc = hinh_thuc
    
    def input_data(self):
        self.__ma_mon = input()
        self.__ten_mon = input()
        self.__hinh_thuc = input()
    
    def printout(self):
        print(self.__ma_mon, self.__ten_mon, self.__hinh_thuc)
    
    def get_ma(self):
        return self.__ma_mon

def cmp(a, b):
    if a.get_ma() < b.get_ma():
        return -1
    elif a.get_ma() > b.get_ma():
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    n = int(input())
    danh_sach_mon_hoc = []

    for i in range(0, n):
        x = monhoc("", "", "")
        x.input_data()
        danh_sach_mon_hoc.append(x)
    
    danh_sach_mon_hoc.sort(key=cmp_to_key(cmp))
    for item in danh_sach_mon_hoc:
        item.printout()
        