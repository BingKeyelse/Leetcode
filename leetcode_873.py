class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        aSet= set(arr)
        check=set() # Dùng để lưu các vị trí đã chạy trước đó 


        pre_val=0
        cur_val=0
        next_val=0
        max_len=2 # tối thiểu phải >= 3 mới tính là chuỗi Fibo

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                len_count=2
                pre_val=arr[i]
                cur_val=arr[j]
                next= pre_val + cur_val
                while next in aSet:
                    len_count+=1
                    pre_val= cur_val
                    cur_val= next
                    next= pre_val + cur_val
                    max_len=max(max_len, len_count)
        print(max_len)
        return max_len if max_len >2 else 0
a= [2,4,7,8,9,10,14,15,18,23,32,50]
Solution().lenLongestFibSubseq(a)
# Solution().lenLongestFibSubseq(eval(input()))


                        

                    


