from collections import deque

#Queue_init

queue = deque()

#Queue_common_methods

#1. push an element

queue.append('Hung')
queue.append('Daskov')
queue.append('Alan')
queue.append('Ducknife')

for item in queue:
    print(item)
    
#2. pop an element

front = queue.popleft()

print('Front of queue is: ', front)

#3. queue size

print(len(queue))

#4. clear queue

queue.clear()

print(len(queue))