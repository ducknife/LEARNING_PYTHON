""" print(object, seperator, end) """
#default 
print('hung', 'rat dep trai') # hung rat dep trai , sep = ' ', end = '\n'
print('hung', 'mot nguoi dep trai', sep = '-', end = ' ') # hung-mot nguoi dep trai va nhat gai
print('va nhat gai') 
print('hung', end = '!\n') # hung! \n rat dep trai
print('rat dep trai')

""" print(cái cần in, phân cách, kết thúc) """

print('Hello Alan') #không có dấu phân cách và dấu kết thúc

print('12', '06', '2005', sep='/') #không có dấu kết thúc, phân cách bằng dấu /

print('Hung muon tro thanh mot', end=' ') #không có phân cách, kết thúc bằng dấu cách
print('AI engineer')

a = 1.23123

print('%.2f' %a) #in ra 2 số thập phân sau dấu phẩy 
print('{:.2f}'.format(a)) #in ra 2 số thập phân sau dấu phẩy

b = 3 + 5j #số thực 

print(b.real) #phần thực
print(b.imag) #phần ảo