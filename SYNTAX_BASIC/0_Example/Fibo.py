fibo = [0] * 100

def setup():
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, 100):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

if __name__ == "__main__":
    setup()
    for i in range(0, 100):
        print(fibo[i])                                            