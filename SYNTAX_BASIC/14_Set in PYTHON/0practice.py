# se = {1, 23, 123, 213, 213}
# se.add(12)
# print(se)
# se.remove(1)
# print(se)
# se.discard(23)
# print(se)
# print(213 in se)

set_A = set()
set_B = set()
union_AB = set()
differ_AB = []
intersec_AB = []
mp = {}

# input_format: 
# first_line: n, m
# second_line: n elements of set_A, m elements of set_B

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        set_A.add(a[i])
        union_AB.add(a[i])
        if not mp.get(a[i]):
            mp[a[i]] = 1
    for i in range(m):
        set_B.add(a[n + i])
        union_AB.add(a[n + i])
        if mp.get(a[n + i]):
            intersec_AB.append(a[n + i])
            mp.pop(a[n + i])
    for x in mp.keys():
        differ_AB.append(x)
    print(sorted(differ_AB))
    print(sorted(intersec_AB))
    print(sorted(list(union_AB)))

# another way to find union and set of set_A and B
# use build-in function 

UNION = set_A.union(set_B)
INTERSEC = set_A.intersection(set_B)
DIFFER = set_A.difference(set_B)
print(UNION, INTERSEC, DIFFER, sep=', ')