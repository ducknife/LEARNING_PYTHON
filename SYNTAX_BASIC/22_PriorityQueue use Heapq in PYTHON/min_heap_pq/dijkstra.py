import heapq as pq

inf = int(1e9)
adj = [[] for _ in range(1005)]
dis = [inf for _ in range(1005)]

class PQ:
    def __init__ (self):
        self.qmin = []
    def push(self, x):
        pq.heappush(self.qmin, x)
    def top(self):
        return self.qmin[0]
    def poptop(self):
        pq.heappop(self.qmin)

def dijkstra(n, m, s):
    dis[s] = 0
    q = PQ()
    q.push((dis[s], s))
    while len(q.qmin):
        top = q.top()
        q.poptop()
        d, u = top
        if d > dis[u]:
            continue
        for w, v in adj[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                q.push((dis[v], v))
    
    for i in range(1, n + 1):
        print(dis[i], end=' ')
    print()

if __name__ == '__main__':
    try:
        t = int(input())
        for _ in range(t):
            n, m, s = map(int, input().split())
            for i in range(1, n + 1):
                dis[i] = inf
                adj[i] = []
            for _ in range(m):
                x, y, w = map(int, input().split())
                adj[x].append((w, y))
                adj[y].append((w, x))
        dijkstra(n, m, s)
    except:
        print('ERROR found baby!')