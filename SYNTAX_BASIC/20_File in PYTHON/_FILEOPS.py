#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    f1 = open('data.inp', 'r')
    f2 = open('data.out', 'w')
    t = int(f1.readline())
    strings = []
    for i in range(t):
        s = f1.readline().strip()
        strings.append(s)
    for s in strings:
        tmp = ' '.join(s.split())
        f2.write(tmp.title())
        f2.write('\n')
        