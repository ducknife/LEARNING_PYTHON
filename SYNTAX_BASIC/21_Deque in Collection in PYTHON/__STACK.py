from collections import deque

#Stack_init

stack = deque()

#Stack_common_methods

#1. push an element

stack.append(12)
stack.append('hung')
stack.append(126)
stack.append(12.6)
stack.append(3 + 5j)

for element in stack:
    print(element)
    
#2. pop an top element

top = stack.pop()

print('Top of stack is: ', top)

#3. stack size

print(len(stack))

#4. clear stack

stack.clear()

print('Length of stack after clear: ', len(stack))
