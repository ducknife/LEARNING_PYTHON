from functools import cmp_to_key

DUCKNIFE = '__main__'

candidates = [
    ["Hannah", 26],
    ["John", 28],
    ["Adam", 25],
    ["David", 29.5],
    ["Maria", 28]
]

def cmp(c_a, c_b):
    if c_a[1] != c_b[1]:
        if c_a[1] < c_b[1]:
            return 1
        else:
            return -1
    if c_a[0] != c_b[0]:
        if c_a[0] < c_b[0]:
            return -1
        else:
            return 1
    return 0

if __name__ == DUCKNIFE:
    #ducknife
    GE25 = list(filter(lambda x : x[1] >= 25, candidates))
    print("Candidates aged 25 and above:" )
    GE25.sort(key=cmp_to_key(cmp))
    for c in GE25:
        print(f'Name: {c[0]}, Score:{c[1]}, Status: {"Passed" if c[1] >= 27 else "Failed"}') 