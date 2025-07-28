
adj = [[] for i in range(0, 1005)]
cc = [[] for i in range(0, 1005)]
visited = [False] * 1005
cnt = 0
found = False

def dfs(u):
    cc[u] = cnt
    visited[u] = True
    for v in adj[u]:
        if visited[v] == False:
            dfs(v)


if __name__ == "__main__":
    n, m, u = map(int, input().split())
    for i in range(0, m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    for i in range(1, n + 1):
        if visited[i] == False:
            cnt += 1
            dfs(i)
    for i in range(1, n + 1):
        if cc[i] != cc[u]:
            found = True
            print(i)
    if found == False:
        print(0)