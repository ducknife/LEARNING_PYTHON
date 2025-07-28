import heapq as pq

class PQ:
    def __init__ (self):
        self.qmax = []

    def push(self, x):
        pq.heappush(self.qmax, -x)

    def poptop(self):
        -pq.heappop(self.qmax)

    def top(self):
        return -self.qmax[0]
    
if __name__ == '__main__':
    q = PQ() #PQ max heap chứa các giá trị negative của giá trị push vào

    q.push(3)
    q.push(2) 
    q.push(-1)
    for x in q.qmax:
        print(x, end=' ')
    print()

    top = q.top()
    print(top) 

    q.poptop()
    for x in q.qmax:
        print(x, end=' ')
