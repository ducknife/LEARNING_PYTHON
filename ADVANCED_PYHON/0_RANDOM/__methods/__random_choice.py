import random

arr = [1, 4, 2, 1, 32, -1]

x = random.choice(arr) #chọn ngẫu nhiên 1 phần tử từ chỗ có sẵn 

print(x)

rand_arr = random.choices(arr, k=4) #chọn ngẫu nhiên 4 phần tử có thể trùng lặp từ chỗ có sẵn 

print(rand_arr)

new_rand_arr = random.choices(arr, k=4)[1] #chọn ngẫu nhiên 4 phần tử có thể trùng lặp và lấy phần tử ở idx 1 

print(new_rand_arr)

not_repeat_arr = random.sample(arr, k=4) #chọn ngẫu nhiên 4 phần tử không lặp lại 

print(not_repeat_arr)

# tạo tỉ lệ cho các phần tử

a_w = [10, 15, 15, 10, 25, 25] #mảng tỉ lệ tương ứng với các phần tử trong arr

fre = {}

for i in range(100):
    xw = random.choices(arr, weights=a_w, k=1)[0] # 32 và -1 có tí lệ chọn trúng cao nhất
    if xw not in fre.keys():
        fre[xw] = 1
    else:
        fre[xw] += 1

for key, val in fre.items():
    print(f'key: {key} appear {val} times')