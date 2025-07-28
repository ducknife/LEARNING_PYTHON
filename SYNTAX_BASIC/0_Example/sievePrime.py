MAXN = int(1e7 + 1)
prime = [True] * MAXN

def sieve ():
    prime[0] = prime[1] = False
    for idx in range(2, MAXN):
        if prime[idx]:
            for j in range (idx * idx, MAXN, idx):
                prime[j] = False



if __name__ == '__main__':
    sieve()
    for i in range (1, int(1e3)):
        if prime[i]:
            print(i, end=" ")

