import os
import json

FILE_PATH = os.path.join(os.path.dirname(__file__), './DATASETS.json')

#os.path.dirname() : trỏ tới thư mục cha. 

def load_data():
    with open(FILE_PATH, 'r') as DATASET:
        return json.load(DATASET)
    
def update_data(user_data):
    with open(FILE_PATH, 'w', encoding='utf-8') as DATASET:
        json.dump(user_data, DATASET, indent=4, ensure_ascii=False, default=str)
    
    #default = str: tự động định dạng
    #ensure_ascii=False: không chuyển tiếng Việt thành mã ascii 
user_data = load_data()

KEY_LEVEL_ONE = 'students'
user_data[KEY_LEVEL_ONE]['age'] = 20
user_data[KEY_LEVEL_ONE]['major'] = 'CS'

update_data(user_data)


