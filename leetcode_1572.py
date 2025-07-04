class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0]) if mat else 0
        print("Số hàng:", rows)
        print("Số cột:", cols)
        
        sum= 0
        for i in range(rows):
            a=i
            b=rows-i-1
            
            if a==b:
                sum+= mat[i][a]
            else:
                sum+= mat[i][a] + mat[i][b]
            
        return sum







a= [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().diagonalSum(a))