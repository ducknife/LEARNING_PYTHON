import random
import json
import pandas

domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com']

pass_rs = 'asdfghjklzxcvbnm?~1234567890!@#4%67*-+'

users = {}

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

first_names = [
    ["Male",
        "James", "John", "Robert", "Michael", "William",
        "David", "Richard", "Joseph", "Thomas", "Charles",
        "Christopher", "Daniel", "Matthew", "Anthony", "Mark"
    ],
    ["Female",
        "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
        "Barbara", "Susan", "Jessica", "Sarah", "Karen",
        "Nancy", "Lisa", "Betty", "Margaret", "Sandra"
    ]
]

for i in range(100):
    last_name = random.choice(last_names)
    choose_sex = random.choice([0, 1])
    first_name = random.choice(first_names[choose_sex])
    sex = None
    if first_name in first_names[1]:
        sex = "male"
    else:
        sex = "female"
    email = first_name.lower() + last_name.lower()
    domain = random.choice(domains)
    # nếu dùng choices thì sẽ bị trùng lặp
    a = random.sample(pass_rs, 16)
    password = ''.join(a)
    data = {
        'email' : email + domain,
        'first_name' : first_name,
        'last_name' : last_name,
        'password' : password,
        'sex' : sex
    }
    users['user_id_' + str(i)] = data

df = pandas.DataFrame.from_dict(users, orient='index')
df.to_csv('users.csv')

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)


