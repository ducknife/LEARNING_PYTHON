import heapq

""" tạo một priority queue min heap với heapq """

pq = []
#thao tac push: them vao pq
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
heapq.heappush(pq, 0)
heapq.heappush(pq, -1)
print(pq) # phan tu nho nhat luon o dau

#thao tac pop: lay va xoa phan tu dau tien
top = heapq.heappop(pq)
print(top) # -1
print(pq)  # phan tu nho nhat luon o dau

#thao tac lay gia tri dau tien pq va khong xoa no
top = pq[0]
print(top) # 0

""" tự định nghĩa các hàm này cho dễ dùng """
def pushq(pq, x):
    heapq.heappush(pq, x)

def popq(pq):
    heapq.heapppop(pq)

def popo(pq):
    return pq[0]

""" ///________________________________________________________________________\\\ """

""" tạo một priority queue max heap với heapq """

""" cần thêm dấu âm những chỗ sau:  """

# thao tác push: thêm dấu âm vào trước x để tạo max heap

pq_mx = []
heapq.heappush(pq_mx, -(1)) # push 1 vào max heap 
heapq.heappush(pq_mx, -(-2)) #push -2 vào max heap 

print(pq_mx) # pq_mx hiện tại là [-1, 2] tuy nhiên khi lấy ra phần tử đầu tiên ta sẽ thêm dấu âm 1 lần nữa
#như trong ví dụ này thì lấy ra số bé nhất là -1 và thêm dấu âm sẽ thành 1 (là số lớn nhất trong max_heap) đúng như
# ta đã thêm vào

# thao tác pop:
print(-heapq.heappop(pq_mx)) #1

#thao tác lấy giá trị lớn nhất và không xóa
heapq.heappush(pq_mx, -3) #push 3 vào max heap 
print(-pq_mx[0]) # 3