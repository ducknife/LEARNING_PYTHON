import os

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    f1 = open('data.out', 'r')
    strings = []
    while True:
        s = f1.readline().strip()
        if s:
            strings.append(s)
        else:
            break
    f2 = open('data.out', 'w')
    for s in strings:
        if 'Hung' in s:
            f2.write(s.replace('Hung', 'Ducknife'))
        else:
            f2.write(s)
        f2.write('\n')