class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        result = []
        n = len(matrix)
        m = len(matrix[0])
        
        # 4 dimensions of the matrix  
        top = 0
        left = 0
        right = m - 1
        bottom = n - 1

        while top <= bottom and left <= right:
            # Traverse right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # Traverse left (if there are rows left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Traverse up (if there are columns left)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
    
    
    
    
    
    