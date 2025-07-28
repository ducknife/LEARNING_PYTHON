
user_list = ['Mai', 'Hung', 'Lan', 'Hieu']

user_list.reverse()
print(user_list)

print(user_list.count('Hung'))
print(user_list.index('Hieu'))

user_list.sort()
print(user_list)

user_list_2 = sorted(user_list)
print(user_list_2)

user_list_3 = user_list[::-1]
print(user_list_3)

user_list[:0] = ['Hong']
print(user_list)

user_list[len(user_list):] = ['Minh']
print(user_list)

print(user_list[0:4])

user_list.pop(1)
print(user_list)

user_list.remove('Mai')
print(user_list)

del user_list[1]

user_list_4 = [user + 'STD' for user in user_list if user.startswith('H')]
print(user_list_4)
