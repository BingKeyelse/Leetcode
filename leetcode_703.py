import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
                
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
objs = ["KthLargest", "add", "add", "add", "add", "add"]
data = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Kết quả lưu đầu ra
res = []

# Biến lưu object KthLargest
obj = None

# Thực hiện từng thao tác
for i in range(len(objs)):
    if objs[i] == "KthLargest":
        obj = KthLargest(*data[i])  # khởi tạo đối tượng duy nhất
        res.append(None)
    else:
        out = obj.add(*data[i])     # gọi add(val)
        res.append(out)

print(res)


