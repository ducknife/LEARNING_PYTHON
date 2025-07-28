import os

""" tao file moi """
f = open("input.txt", "x")
f.close()



""" doc file """
f = open("input.txt", "r")
print(f.read())
print(f.read(2)) #chi doc 2 ki tu
print(f.readline()) #in ra dong dau tien
f.close()



""" ghi file """
f = open("input.txt", "w")
f.write("AI and Machine learning") #f.write() only accept one argument
f.write(' hello hee')
f.close()



if os.path.exists("input.txt"):
    print(True)
else:
    print(False)
    
    
    
print(os.path.join(os.path.dirname(__file__), './_DATASETS.json')) 

""" os.path.dirname(__file__): lấy đường dẫn thư mục chứa file """

""" os.remove("input.txt") """