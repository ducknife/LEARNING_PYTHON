class Node:
    def __init__(self, data, next):
        self.data = None
        self.next = None

def make_node(data):
    new_node = Node('', '')
    new_node.data = data
    return new_node

def traverse(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end=' ')
        tmp = tmp.next
        if tmp != None: 
            print('->', end=' ')
    
if __name__ == '__main__':
    a = list(map(int, input().split()))
    head = make_node(a[0])
    tmp = head
    for x in a:
        tmp.next = make_node(x)
        tmp = tmp.next
    traverse(head)