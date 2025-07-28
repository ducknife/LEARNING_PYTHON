from binary_search import binary_search as bs

f = open('input.txt', 'r')
a = list(map(int, f.readline().split()))
a.sort()
fw = open('output.txt', 'w')
fw.write(str(a))
print(bs(a, 0, 3, -1))
f.close()



