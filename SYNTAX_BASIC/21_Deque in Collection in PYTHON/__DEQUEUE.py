from collections import deque

#deque_init

dq = deque()

#deque_common_methods

#1. push_back, push_front

#push_back
dq.append(1)
dq.append('Hung')
dq.append(2)

#push_front
dq.appendleft('Daskov')
dq.appendleft(6)

for item in dq:
    print(item)
    
#2. pop_back, pop_front

#pop_back
back = dq.pop()

#pop_front
front = dq.popleft()

print(front, back)

#3. deque size

print(len(dq))

#4. clear deque

dq.clear()

print(dq)