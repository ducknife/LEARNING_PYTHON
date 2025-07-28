from collections import deque
# from collections import Counter

DUCKNIFE = '__main__'

def gen(n):
    cnt = 0
    q = deque()
    q.append(['A', 1, 0, 0])
    q.append(['B', 0, 1, 0])
    q.append(['C', 0, 0, 1])
    while len(q) > 0:
        x = q.popleft()
        if len(x[0]) > n:
            continue
        if x[1] and x[1] <= x[2] and x[2] <= x[3]:
            # print(x[0])
            cnt += 1
        q.append([x[0] + 'A', x[1] + 1, x[2], x[3]])
        q.append([x[0] + 'B', x[1], x[2] + 1, x[3]])
        q.append([x[0] + 'C', x[1], x[2], x[3] + 1])
    print(cnt)

if __name__ == DUCKNIFE:
    n = int(input())
    gen(n)