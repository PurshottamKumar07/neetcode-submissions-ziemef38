class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n=len(matrix),len(matrix[0])
        
        def bs(low,high):

            if low>high:
                return False
            
            mid=low+(high-low)//2

            r=mid//n
            c=mid%n

            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                return bs(low,mid-1)
            else:
                return bs(mid+1,high) 
        
        return bs(0,m*n-1)