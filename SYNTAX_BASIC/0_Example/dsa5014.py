C = [0] * 101
def setup():
    C[0] = C[1] = 1
    C[2] = 2
    for i in range(3, 101):
        for j in range(0, i):
            C[i] += C[j] * C[i - j - 1]

setup()
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(C[n])
