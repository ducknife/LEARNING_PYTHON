f = [0] * 100

def setup():
    f[0] = f[1] = 1;
    f[2] = 2
    for i in range(3, 100):
        f[i] = f[i - 1] + f[i - 2] + f[i - 3]
    

if __name__ == "__main__":
    setup()
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        print(f[n])
    