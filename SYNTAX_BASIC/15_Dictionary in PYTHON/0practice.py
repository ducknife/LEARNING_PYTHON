user_data = {
    'username' : 'Daskov Niev',
    'password' : 'hung126@',
    'birthday' : '12/06/2005',
    'major' : 'IT',
    'job' : 'AI engineer'
}

print(user_data['username'])
print(user_data.get('password'))

user_keys = list(user_data.keys())
print(user_keys)

user_values = list(user_data.values())
print(user_values)

user_items = list(user_data.items())
print(user_items)

user_data['age'] = 20
print(user_data)

user_data.pop('age')
print(user_data)

del user_data['birthday']
print(user_data)

user_data.popitem()
print(user_data)

user_data.clear();
print(user_data)

user_data = dict(zip(user_keys, user_values))
print(user_data)

user_data = dict.fromkeys(user_keys, None)
print(user_data)


def name(x):
    return 'Hung' + str(x)
user_data = {name(x) : name(x + 1) for x in range(0, 10)}
print(user_data)

print(user_data.popitem())