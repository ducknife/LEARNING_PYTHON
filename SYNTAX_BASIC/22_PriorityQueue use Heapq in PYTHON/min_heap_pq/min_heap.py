import heapq as pq

class PQ:
    def __init__(self):
        self.qmin = []

    def push(self, x):
        pq.heappush(self.qmin, x)

    def poptop(self):
        pq.heappop(self.qmin)

    def top(self):
        return self.qmin[0]


if __name__ == '__main__':
    q = PQ()
    q.push(2)
    q.push(1)
    q.push(-1)

    for x in q.qmin:
        print(x, end=' ')
    print()

    top = q.top()
    print(top)

    q.poptop()
    
    for x in q.qmin:
        print(x, end=' ')



