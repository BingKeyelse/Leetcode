class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows= len(matrix)
        cols= len(matrix[0])
        new_mtx=[]
        for i in range(cols):
            restored=[]
            for j in range(rows):
                restored.append(matrix[j][i])
            
            new_mtx.append(restored)
        return new_mtx
       
                
# a=[[1,2,3],[4,5,6],[7,8,9]]
a= [[1,2,3],[4,5,6]]
print(Solution().transpose(a))
