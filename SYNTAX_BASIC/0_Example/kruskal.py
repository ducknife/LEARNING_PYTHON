from functools import cmp_to_key

parent = [0] * 1005
size = [0] * 1005
edges = []

def INIT(n):
    for i in range(1, n + 1):
        parent[i] = i
        size[i] = 1

def FIND(u):
    if u == parent[u]:
        return u
    else:
        parent[u] = FIND(parent[u])
        return parent[u]

def UNION(u, v):
    u = FIND(u)
    v = FIND(v)
    if u == v:
        return False
    if size[u] < size[v]:
        u, v = v, u
    size[u] += size[v]
    parent[v] = u
    return True

def cmp(a, b):
    if a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1
    else:
        return 0

def kruskal(n, m):
    MST = []
    res = 0
    edges.sort(key=cmp_to_key(cmp))
    for i in range(0, m):
        if len(MST) == n - 1:
            break
        elif UNION(edges[i][0], edges[i][1]) == True:
            MST.append(edges[i])
            res += edges[i][2]
    
    print(res)


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n, m = map(int, input().split())
        INIT(n)
        for i in range(1, m + 1):
            x, y, w = map(int, input().split())
            edges.append((x, y, w))
        kruskal(n, m)
        edges.clear()