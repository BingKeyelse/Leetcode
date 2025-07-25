class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range (i+1, len(matrix)):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
    
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        return matrix
    
a=[[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(a))