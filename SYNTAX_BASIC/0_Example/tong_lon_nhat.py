import os

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    file_path = os.path.join(os.path.dirname(__file__), 'INPUT.txt')
    f = open(file_path, 'r')
    t = int(f.readline())
    for _ in range(t):
        a, b = map(list, f.readline().strip().split())
        for i in range(len(a)):
            if a[i] == '6':
                a[i] = '8'
        for i in range(len(b)):
            if b[i] == '6':
                b[i] = '8'
        sa, sb = int(''.join(a)), int(''.join(b))
        print(sa + sb)
    f.close()
