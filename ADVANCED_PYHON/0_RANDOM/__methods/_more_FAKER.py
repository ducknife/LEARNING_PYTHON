from faker import Faker
import json
import os

fake = Faker("vi_VN")  # locale tiếng Việt

users = {}

for i in range(5):
    user =  {
        'name' : fake.name(),
        'first name' : fake.first_name(),
        'last name' : fake.last_name(),
        'date of birth' : fake.date_of_birth(minimum_age=18, maximum_age=20),
        'address' : fake.address(),
        'country' : fake.country(),
        'city' : fake.city(),
        'phone number' : fake.phone_number(),
        'email' : fake.email(),
        'domain' : fake.domain_name(),
        'url' : fake.url(),
        'user name' : fake.user_name(),
        'company' : fake.company(),
        'job' : fake.job(),
        'profile' : fake.profile()
    }
    users[f'user{i}'] = user

path = os.path.join(os.path.dirname(__file__), './user_data.json')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(users, f, indent=4, ensure_ascii=False, default=str) 

    #ensure_ascii = False là không chuyển tiếng Việt thành mã ascii
    #default = str để tự động đọc các định dạng 
