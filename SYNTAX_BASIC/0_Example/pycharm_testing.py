import json
import os

DUCKNIFE = '__main__'

PATH = os.path.join(os.path.dirname(__file__), './judge.json')

def load_data():
    with open(PATH, 'r') as f:
        return json.load(f)

judge_list = load_data()

def write_judge():
    with open(PATH, 'w') as f:
        json.dump(judge_list, f, indent=4)

if __name__ == DUCKNIFE:
    user_judge = input()

    if 'lag' in user_judge.lower():
        judge_list['Lag'] += 1
    elif 'stable' in user_judge.lower():
        judge_list['Stable'] += 1
    elif 'smooth' in user_judge.lower():
        judge_list['Smooth'] += 1

    write_judge()
