class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new= nums+nums
        print(new)

        stack =[]
        store =[]  ## dùng để lưu kết quả 

        for idx in range(len(new)-1, -1, -1):
            print(new[idx])
            if not stack:
                store.append(-1)
                stack.append(new[idx])
            else:
                while stack:
                    if new[idx] >=stack[-1]:
                        stack.pop()
                    else:
                        store=[stack[-1]]+store
                        stack.append(new[idx])
                        break

                if not stack:
                    store=[-1]+store
                    stack.append(new[idx])
        
        return store[0:len(nums)]