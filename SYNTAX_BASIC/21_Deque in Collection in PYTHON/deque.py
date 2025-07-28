from collections import deque

#hang doi, hang doi hai dau, stack deu co the bieu dien bang deque
""" cac phuong thuc cua deque trong collection """

dq = deque() #khoi tao deque
dq.append(1) #them 1 vao cuoi hang doi
dq.appendleft(0) #them 0 vao dau hang doi
dq.pop() #lay ra phan tu cuoi hang doi va xoa no di
dq.popleft() #lay ra phan tu dau hang doi va xoa no di
dq.clear() #xoa het
dq.copy() #tao mot ban sao khac

""" ///________________________________________________________________________\\\ """

""" tao mot queue don gian """
queue = deque()

#them phan tu vao queue
queue.appendleft(1)
queue.appendleft(2) 
print(queue) # [2, 1]

#pop va lay ra phan tu dau hang doi
x = queue.pop()
print('gia tri cuoi hang doi la:', x) # 1

queue.append(3)
print(queue) # [2, 3]

y = queue.popleft()
print('gia tri dau hang doi la:', y) # 2
print()

""" ///________________________________________________________________________\\\ """

""" tao mot stack don gian """
stack = deque()

#them phan tu vao stack
stack.append(1)
stack.append(2)
print(stack) # [1, 2]

#pop va lay ra phan tu dinh stack
top = stack.pop()
print('gia tri tai dinh stack la:', top)
print()

""" ///________________________________________________________________________\\\ """