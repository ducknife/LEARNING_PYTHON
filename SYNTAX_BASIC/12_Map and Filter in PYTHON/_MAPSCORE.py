from functools import cmp_to_key

DUCKNIFE = '__main__'

candidates = [
    ["Hannah", 26],
    ["John", 28],
    ["Adam", 25],
    ["David", 29.5],
    ["Maria", 28]
]

def add_one(x):
    x[1] += 0.25 * x[1]
    return x

if __name__ == DUCKNIFE:
    #ducknife
    GE25 = list(map(lambda x : add_one(x), candidates))
    print("Candidates aged 25 and above:" )
    for c in GE25:
        print(f'Name: {c[0]}, Score:{c[1]:.2f}, Status: {"Passed" if c[1] >= 35 else "Failed"}') 